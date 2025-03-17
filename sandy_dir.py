import backtrader as bt
import inspect

def print_classes_and_methods(module):
    """
    Prints the classes, subclasses, and methods within a given module,
    labeling methods with their corresponding subclasses.

    Args:
        module: The module to inspect (e.g., backtrader).
    """

    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            print(f"Class: {name}")

            # Get the base classes of the current class
            base_classes = obj.__bases__

            for method_name, method in inspect.getmembers(obj):
                if inspect.isfunction(method) and not method_name.startswith('_'):
                    # Find the base class where the method is defined
                    defining_class = None
                    for base in base_classes:
                        if hasattr(base, method_name) and inspect.getattr_static(obj, method_name) is getattr(base, method_name):
                            defining_class = base.__name__
                            break

                    if defining_class:
                        print(f"  Method: {method_name} (from {defining_class})")
                    else:
                        print(f"  Method: {method_name}")

# Print the classes and methods of the backtrader module
print_classes_and_methods(bt)
