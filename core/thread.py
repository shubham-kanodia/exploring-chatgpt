class Thread:
    def __init__(self, client, role=None, content=None, file_ids=None, thread_id=None):
        self.client = client

        if not thread_id:
            self.thread = client.beta.threads.create(
                messages=[
                    {
                        "role": role,
                        "content": content,
                        "file_ids": file_ids
                    }
                ]
            )

            self.thread_id = self.thread.id

        else:
            self.thread_id = thread_id

    def get_id(self):
        return self.thread_id

    def get_all_messages(self):
        messages = self.client.beta.threads.messages.list(thread_id=self.thread_id)
        messages_id = [message.id for message in messages.data]

        processed_messages = []

        for message_id in messages_id:
            message = self.client.beta.threads.messages.retrieve(
                message_id=message_id,
                thread_id=self.thread_id
            )

            processed_messages.append(message.content[0].text.value)

        return processed_messages
