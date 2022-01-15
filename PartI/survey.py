class AnonymousSurvey:
    """Collect anonymous answer to a survey question."""


    def __init__(self, question):
        """Store a question, and prepare to store response."""

        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""

        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""

        self.responses.append(new_response)

    def show_results(self):
        """Show all the response that have been given."""

        print("survey results:")
        for response in self.responses:
            print(f" - {response}")
