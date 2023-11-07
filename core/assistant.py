from openai._types import NOT_GIVEN


class Assistant:
    def __init__(self, client, instructions, model_identifier, tools, file_ids=NOT_GIVEN):
        self.assistant = client.beta.assistants.create(
            instructions=instructions,
            model=model_identifier,
            tools=tools,
            file_ids=file_ids
        )

        self.assistant_id = self.assistant.id

    def get_id(self):
        return self.assistant_id
