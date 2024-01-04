from PyQt6.QtWidgets import QApplication, QLabel, \
    QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox
import sys


class AverageSpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # Create widgets
        distance_label = QLabel("Distance:")
        self.distance_line_edit = QLineEdit()

        time_label = QLabel("Time (hours):")
        self.time_label_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")

        self.imperial_or_metric = QComboBox()
        self.imperial_or_metric.addItem("Imperial(miles)")
        self.imperial_or_metric.addItem("Metric (km)")

        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_label_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)
        grid.addWidget(self.imperial_or_metric, 0, 3, 1, 2)
        grid.addWidget(self.output_label, 3, 3)
        self.setLayout(grid)

    def calculate_speed(self):
        distance = self.distance_line_edit.text()
        time = self.time_label_line_edit.text()
        total_speed = float(distance) / float(time)
        total_speed = str(total_speed)
        self.output_label.setText(total_speed)


app = QApplication(sys.argv)
average_speed_calculator = AverageSpeedCalculator()
average_speed_calculator.show()
sys.exit(app.exec())
