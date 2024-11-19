import matplotlib.pyplot as plt
import matplotlib.patches as patches


class FibonacciResearchColors:
    def __init__(self):
        self.deep_black = "#000000"
        self.golden_yellow = "#FFD700"
        self.dark_slate_gray = "#2F4F4F"
        self.ivory = "#FFFFF0"
        self.fibonacci_blue = "#0066CC"
        self.sage_green = "#8FBC8F"

    def get_color_dict(self):
        return {
            "Deep Black": self.deep_black,
            "Golden Yellow": self.golden_yellow,
            "Dark Slate Gray": self.dark_slate_gray,
            "Ivory": self.ivory,
            "Fibonacci Blue": self.fibonacci_blue,
            "Sage Green": self.sage_green,
        }

    def display_colors(self):
        colors = self.get_color_dict()
        fig, ax = plt.subplots(figsize=(10, 6))
        y_offset = 0
        for color_name, color_code in colors.items():
            rect = patches.Rectangle((0, y_offset), 1, 1, facecolor=color_code)
            ax.add_patch(rect)
            ax.text(
                1.1,
                y_offset + 0.5,
                f"{color_name} ({color_code})",
                va="center",
                ha="left",
                fontsize=12,
            )
            y_offset += 1

        ax.set_xlim(0, 3)
        ax.set_ylim(0, len(colors))
        ax.axis("off")
        plt.title("Fibonacci Research Color Palette", fontsize=16)
        plt.tight_layout()
        plt.show()


# Usage example
if __name__ == "__main__":
    fr_colors = FibonacciResearchColors()
    fr_colors.display_colors()

    # Example of how to use the colors in your code
    print("Using Deep Black:", fr_colors.deep_black)
    print("Using Golden Yellow:", fr_colors.golden_yellow)

    # You can also access colors using the dictionary
    color_dict = fr_colors.get_color_dict()
    print("Fibonacci Blue from dict:", color_dict["Fibonacci Blue"])
