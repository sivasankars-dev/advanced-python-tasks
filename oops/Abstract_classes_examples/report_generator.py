# Scenario:
# You’re building a reporting system with a common structure: a header, a body, and a footer.
# ✅ Requirements:
# Create an abstract class ReportGenerator:
# It has a concrete method generate_header()
# It has an abstract method generate_body()
# It has a concrete method generate_footer()
# Create a subclass SalesReport that implements generate_body().
# Write a method generate_full_report(report) that calls all 3 methods in order.

from abc import ABC, abstractmethod

class ReportGenerator(ABC):
    def generate_header(self):
        print("This is Header")

    @abstractmethod
    def generate_body(self):
        pass

    def generate_footer(self):
        print("This is body")

    def generate_full_report(self, bodydata):
        self.generate_header()
        self.generate_body(bodydata)
        self.generate_footer()

class SalesReport(ReportGenerator):
    def generate_body(self, data):
        print(f"Hi welcome to this {data}")

report1 = SalesReport()
report1.generate_full_report('sales report')
