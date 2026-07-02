from client import ShippingEstimatorClient
def main():
    c = ShippingEstimatorClient()
    print(c.estimate_shipping(5.4, "90210", "10001"))
if __name__ == '__main__':
    main()
