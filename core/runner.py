class Runner:
    def __init__(self, client, thread_id, assistant_id):
        self.client = client
        self.thread_id = thread_id
        self.assistant_id = assistant_id

    def run(self):
        run = self.client.beta.threads.runs.create(
            thread_id=self.thread_id,
            assistant_id=self.assistant_id
        )

        print(run)
