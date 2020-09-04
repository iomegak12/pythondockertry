from injector import Injector, Inject
import crmsystem


def configure(binder):
    binder.bind(crmsystem.CustomerService,
                to=crmsystem.CustomerService(lambda customers:
                                             print(crmsystem.PrettyTableGenerator.get_customer_table(customers))))

    binder.bind(crmsystem.OrderService,
                to=crmsystem.OrderService(lambda orders:
                                          print(crmsystem.PrettyTableGenerator.get_order_table(orders))))


def main():
    injector = Injector([configure])
    dataController = injector.get(crmsystem.DataController)

    dataController.process(
        lambda: print('Both Customer and Order Services Completed Processing!'))


if __name__ == "__main__":
    main()
