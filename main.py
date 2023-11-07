from openai import OpenAI
from dotenv import load_dotenv

from core.assistant import Assistant
from core.thread import Thread
from core.runner import Runner

from time import sleep

load_dotenv()

client = OpenAI()

assistant_instructions = "You are a MLOPs expert"
model = "gpt-4-1106-preview"
tools = [{"type": "code_interpreter"}]


role = "user"
content = "Find 3 unsolved problems in this spaces"

file = client.files.create(
  file=open("res/context.pdf", "rb"),
  purpose='assistants'
)

thread = Thread(
  client=client,
  role=role,
  content=content,
  file_ids=[file.id]
)

assistant = Assistant(
  client=client,
  instructions=assistant_instructions,
  model_identifier=model,
  tools=tools
)

runner = Runner(
  client=client,
  thread_id=thread.get_id(),
  assistant_id=assistant.get_id()
)
runner.run()

sleep(30)

thread = Thread(client=client, thread_id=thread.get_id())
print(thread.get_all_messages())
