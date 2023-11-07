# Exploring ChatGPT

### Setup

* Create a python virtual environment

```commandline
python3 -m venv venv
```

* Activate the virtual environment

```commandline
source venv/bin/activate
```

* Install the requirements

```commandline
pip install -r requirements.txt
```

* Create a `.env` file and add the following line. Place your key instead of `OUR_OPENAI_API_KEY`. You can obtain your keys from [this page](https://platform.openai.com/api-keys) if you don't have one already.

```
OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
```

## Summary

The flow contains three main components:

* [Assistant](core/assistant.py)
* [Thread](core/thread.py)
* [Runner](core/runner.py)

**Assistant:** The assistant contains the instructions, model and tools to use.

**Thread:** The thread represents a conversation session between assistant and user. It holds the messages and other context information related to that session. 

**Run:** Assistants and threads provide context while the actual execution happens using Runs. Run is responsible for executing the thread and has multiple statuses like queued, in_progress, completed, failed etc indicating its lifecycle.

