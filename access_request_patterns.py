class AccessRequest:
    def __init__(self, name, student_id, email, resource, reason):
        self.name = name
        self.student_id = student_id
        self.email = email
        self.resource = resource
        self.reason = reason


# BUILDER PATTERN: Builds and validates an access request
class AccessRequestBuilder:
    def __init__(self):
        self.name = ""
        self.student_id = ""
        self.email = ""
        self.resource = ""
        self.reason = ""

    def set_name(self, name):
        self.name = name
        return self

    def set_student_id(self, student_id):
        self.student_id = student_id
        return self

    def set_email(self, email):
        self.email = email
        return self

    def set_resource(self, resource):
        self.resource = resource
        return self

    def set_reason(self, reason):
        self.reason = reason
        return self

    def build(self):
        if not self.name or not self.student_id or not self.email:
            raise ValueError("Name, Student ID and Email are required.")

        if "@" not in self.email:
            raise ValueError("Enter a valid email address.")

        if not self.resource or not self.reason:
            raise ValueError("Resource and reason are required.")

        return AccessRequest(
            self.name, self.student_id, self.email,
            self.resource, self.reason
        )


# COMMAND PATTERN: Submits and undoes an access request
class SubmitRequestCommand:
    def __init__(self, request, submitted_requests):
        self.request = request
        self.submitted_requests = submitted_requests

    def execute(self):
        self.submitted_requests.append(self.request)
        print("Access request submitted successfully.")

    def undo(self):
        if self.request in self.submitted_requests:
            self.submitted_requests.remove(self.request)
            print("Submission undone. Request removed.")


# Main program
try:
    request = (AccessRequestBuilder()
               .set_name(input("Enter student name: "))
               .set_student_id(input("Enter student ID: "))
               .set_email(input("Enter email: "))
               .set_resource(input("Enter resource (Library/Lab/Portal): "))
               .set_reason(input("Enter reason: "))
               .build())

    submitted_requests = []

    command = SubmitRequestCommand(request, submitted_requests)

    command.execute()

    print("Student:", request.name)
    print("Resource:", request.resource)
    print("Total submitted requests:", len(submitted_requests))

    choice = input("Undo submission? (yes/no): ").lower()
    if choice == "yes":
        command.undo()
        print("Total submitted requests:", len(submitted_requests))

except ValueError as error:
    print("Request validation failed:", error)
