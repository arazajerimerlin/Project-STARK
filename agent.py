from dotenv import load_dotenv
from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions, ChatContext
from livekit.plugins import noise_cancellation, google

from prompts import AGENT_INSTRUCTIONS, SESSION_INSTRUCTIONS


load_dotenv()

class Assistant(Agent):
    def __init__(self, chat_ctx=None) -> None:
        super().__init__(
            instructions=AGENT_INSTRUCTIONS,llm=google.beta.realtime.RealtimeModel(
            voice="Enceladus",
            temperature=0.9,
        )


async def entrypoint(ctx: agents.JobContext):

    session = AgentSession(

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

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))

