from modals.customer import Customer
from modals.coffee import Coffee
from modals.order import Order
from modals.exceptions import ValidationError

class CoffeeShopDebugger:
    """Interactive debug console for coffee shop system"""
    
    def __init__(self):
        self.customers = []
        self.coffees = []
        self._setup_commands()
        
    def _setup_commands(self):
        """Initialize available commands"""
        self.commands = {
            'create_customer': {
                'help': 'Create a new customer: create_customer <name>',
                'method': self._create_customer
            },
            'create_coffee': {
                'help': 'Create a new coffee: create_coffee <name>',
                'method': self._create_coffee
            },
            'create_order': {
                'help': 'Create an order: create_order <customer_name> <coffee_name> <price>',
                'method': self._create_order
            },
            'list_customers': {
                'help': 'List all customers',
                'method': self._list_customers
            },
            'list_coffees': {
                'help': 'List all coffees',
                'method': self._list_coffees
            },
            'list_orders': {
                'help': 'List all orders',
                'method': self._list_orders
            },
            'customer_stats': {
                'help': 'Show customer stats: customer_stats <name>',
                'method': self._customer_stats
            },
            'coffee_stats': {
                'help': 'Show coffee stats: coffee_stats <name>',
                'method': self._coffee_stats
            },
            'help': {
                'help': 'Show this help message',
                'method': self._show_help
            },
            'exit': {
                'help': 'Exit the debug console',
                'method': None
            }
        }

    def run(self):
        """Main debug console loop"""
        print("=== Coffee Shop Debug Console ===")
        self._show_help()
        
        while True:
            try:
                user_input = input("\n> ").strip()
                if not user_input:
                    continue
                    
                parts = user_input.split()
                cmd = parts[0].lower()
                args = parts[1:]
                
                if cmd == 'exit':
                    print("Exiting debug console...")
                    break
                    
                if cmd in self.commands:
                    self.commands[cmd]['method'](*args)
                else:
                    print(f"Unknown command: {cmd}. Type 'help' for available commands.")
                    
            except ValidationError as e:
                print(f"Validation Error: {e}")
            except Exception as e:
                print(f"Error: {e}")

    # Command implementations
    def _create_customer(self, *name_parts):
        """Create a new customer"""
        name = ' '.join(name_parts)
        if not name:
            raise ValidationError("Customer name cannot be empty")
            
        customer = Customer(name)
        self.customers.append(customer)
        print(f"Created customer: {customer.name}")

    def _create_coffee(self, *name_parts):
        """Create a new coffee type"""
        name = ' '.join(name_parts)
        if not name:
            raise ValidationError("Coffee name cannot be empty")
            
        coffee = Coffee(name)
        self.coffees.append(coffee)
        print(f"Created coffee: {coffee.name}")

    def _create_order(self, customer_name, coffee_name, price_str):
        """Create a new order"""
        try:
            customer = self._find_customer(customer_name)
            coffee = self._find_coffee(coffee_name)
            price = float(price_str)
            
            order = Order(customer, coffee, price)
            print(f"Created order: {order}")
            
        except ValueError:
            raise ValidationError("Price must be a number")

    def _list_customers(self):
        """List all customers"""
        print("\nCustomers:")
        for i, customer in enumerate(self.customers, 1):
            print(f"{i}. {customer.name}")

    def _list_coffees(self):
        """List all coffee types"""
        print("\nCoffees:")
        for i, coffee in enumerate(self.coffees, 1):
            print(f"{i}. {coffee.name}")

    def _list_orders(self):
        """List all orders"""
        print("\nOrders:")
        for i, order in enumerate(Order.all_orders, 1):
            print(f"{i}. {order}")

    def _customer_stats(self, *name_parts):
        """Show statistics for a customer"""
        name = ' '.join(name_parts)
        customer = self._find_customer(name)
        
        print(f"\nStats for {customer.name}:")
        print(f"Total orders: {len(customer.orders())}")
        print(f"Coffees ordered: {', '.join(c.name for c in customer.coffees())}")

    def _coffee_stats(self, *name_parts):
        """Show statistics for a coffee"""
        name = ' '.join(name_parts)
        coffee = self._find_coffee(name)
        
        print(f"\nStats for {coffee.name}:")
        print(f"Total orders: {coffee.num_orders()}")
        print(f"Average price: £{coffee.average_price():.2f}")
        
        aficionados = Customer.most_aficionado(coffee)
        if aficionados:
            names = ', '.join(c.name for c in aficionados)
            print(f"Top customer(s): {names}")

    def _show_help(self):
        """Display help information"""
        print("\nAvailable commands:")
        for cmd, info in self.commands.items():
            print(f"  {info['help']}")

    # Helper methods
    def _find_customer(self, name):
        """Find customer by name"""
        for customer in self.customers:
            if customer.name.lower() == name.lower():
                return customer
        raise ValidationError(f"Customer '{name}' not found")

    def _find_coffee(self, name):
        """Find coffee by name"""
        for coffee in self.coffees:
            if coffee.name.lower() == name.lower():
                return coffee
        raise ValidationError(f"Coffee '{name}' not found")

if __name__ == "__main__":
    debugger = CoffeeShopDebugger()
    debugger.run()