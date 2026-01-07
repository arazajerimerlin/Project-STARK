from dotenv import load_dotenv
from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions, ChatContext
from livekit.plugins import noise_cancellation, google

from prompts import AGENT_INSTRUCTIONS, SESSION_INSTRUCTIONS
from tools import get_weather, search_web
from mem0 import AsyncMemoryClient
import json
import logging


load_dotenv()

class Assistant(Agent):
    def __init__(self, chat_ctx=None) -> None:
        super().__init__(
            instructions=AGENT_INSTRUCTIONS,llm=google.beta.realtime.RealtimeModel(
            voice="Enceladus",
            temperature=0.9,
        ),
            tools=[
                get_weather,
                search_web,
                ],
                chat_ctx=chat_ctx
        )

async def shutdown_hook(chat_ctx: ChatContext, mem0: AsyncMemoryClient, memory_str: str):
    logging.info("Shutting down, saving chat context to memory...")

    messages_formatted = [
        ]

    logging.info(f"chat context messages: {chat_ctx.items}")

    for item in chat_ctx.items:
        content_str = ''.join(item.content) if isinstance(item.content, list) else str(item.content)

        if memory_str and memory_str in content_str:
                continue

        if item.role in ['user', 'assistant']:
            messages_formatted.append({
                "role": item.role,
                "content": content_str.strip()
            })
    logging.info(f"formated messages to add to memory: {messages_formatted}")
    await mem0.add(messages_formatted, user_id="Yuri")
    logging.info("Chat context saved to memory.")


async def entrypoint(ctx: agents.JobContext):

    session = AgentSession(

    )

    mem0 = AsyncMemoryClient()
    user_name = 'Yuri'

    results = await mem0.get_all(user_id=user_name)
    initial_ctx = ChatContext()
    memory_str = ''

    if results:
        memories = [
            {
                "memory": results["memory"],
                "updated_at": results["updated_at"]
            }
            for results in results
        ]
        memory_str = json.dumps(memories)
        logging.info(f"Memories: {memory_str}")
        initial_ctx.add_message(
            role="assistant",
            content=f"the user's name is {user_name}, and this is relevant context about him: {memory_str}",
        )

    await session.start(
        room=ctx.room,
        agent=Assistant(chat_ctx=initial_ctx),
        room_input_options=RoomInputOptions(
            video_enabled=True,
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    await ctx.connect()


    reply_text = await session.generate_reply(
        instructions=SESSION_INSTRUCTIONS
    )

    ctx.add_shutdown_callback(lambda: shutdown_hook(session._agent.chat_ctx, mem0, memory_str))

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
