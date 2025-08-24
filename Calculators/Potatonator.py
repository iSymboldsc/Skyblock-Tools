import questionary as q
from rich.console import Console
from rich.table import Table

console = Console()

def Main():
    console.print(
        """\nWelcome to the [bold]Potatoer[/bold] [italic](Official name trust)[/italic]

So I'm going to [italic]set some things[/italic], you might want to know:

1. Make sure that when you say your [bold]Hourly rate[/bold], 
   it's in [bold]🥔 [italic]Enchanted Potatoes[/italic] 🥔[/bold] and your most [bold]recent[/bold] one.
"""
    )

    Quantity_Armor = q.text("How many Pieces of Armor or Bows / Swords are you going to be using the books in?",
                            validate=lambda numbery: True if numbery=="" or numbery.isdigit() else "Only normal numbers >:(" ).ask()
    
    Quantity_Books = q.text("How many books are you going to use / piece?",
                            validate=lambda numbery: True if numbery=="" or numbery.isdigit() else "Only normal numbers >:(" ).ask()
    Hourly_Rate = q.text("What your Potato hourly rate?").ask()
        
    Quantity_Books = int(Quantity_Books)
    Quantity_Armor = int(Quantity_Armor)
    Hourly_Rate = int(Hourly_Rate)
    AmountBooks = Quantity_Armor * Quantity_Books

    Calculations = Table(title="Potatoer Calculations")
    Calculations.add_column("Type", style='cyan')
    Calculations.add_column("Amount of Books", style='purple')
    Calculations.add_column("Regular Potatoes", style='#8B4513')
    Calculations.add_column("Enchanted Potatoes", style='#FFA500') # Style is orange, only that it isn't a built-in color.
    Calculations.add_column("Enchanted Bakes Potatoes", style='#FFFF00') # Style is yellow (yes, yellow is built-in), but it's too "unbright"

    Calculations.add_row("Example", "1 Book", str(160**2) + " Potatoes", "160 Potatoes", "1 Potatoes")
    Calculations.add_row("Needed for each Piece",str(Quantity_Books) + " Books", str(Quantity_Books * 160**2) + " Potatoes", str(Quantity_Books * 160) + " Potatoes", str(Quantity_Books) + " Potatoes")
    Calculations.add_row("Total", str(AmountBooks) + " Books", str(AmountBooks * 160**2) + " Potatoes", str(AmountBooks * 160) + " Potatoes",  str(AmountBooks) + " Potatoes")
    Calculations.add_row("Hourly Rate", str(Hourly_Rate / 160) + " Books", str(Hourly_Rate * 160) + " Potatoes", str(Hourly_Rate) + " Potatoes", str(Hourly_Rate / 160) + " Potatoes")

    console.print(Calculations)
    console.print("It will take around [bold]" + str(40 / (Hourly_Rate / 160)) + " Hours")
    

if __name__ == '__main__':
    Main()
