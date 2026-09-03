
"""
We should prevent code duplication for every task we have to execute auditTrail

We Also should prevent the structure difference maybe later the other task will be designed differently
"""


from abc import ABC, abstractmethod


class Task(ABC):

    def __init__(self, audit_trail):
        self._audit_trail = audit_trail

    # TEMPLATE METHOD
    def execute(self):
        self._audit_trail.record()
        self.do_execute()

    @abstractmethod
    def do_execute(self):
        pass


class TransferMoneyTask(Task):

    def do_execute(self):
        print("Transfer Money")


class GenerateReportTask(Task):

    def do_execute(self):
        print("Generate Report")


class AuditTrail:

    def record(self):
        print("audit")


if __name__ == "__main__":
    audit_trail = AuditTrail()

    transfer = TransferMoneyTask(audit_trail)
    transfer.execute()

    report = GenerateReportTask(audit_trail)
    report.execute()
