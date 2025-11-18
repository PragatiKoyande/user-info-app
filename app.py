import argparse

def main():
    parser = argparse.ArgumentParser(description="User Info App")
    parser.add_argument("--first_name", required=True)
    parser.add_argument("--last_name", required=True)
    parser.add_argument("--street", required=True)
    parser.add_argument("--city", required=True)
    parser.add_argument("--state", required=True)

    args = parser.parse_args()

    print(f"Full Name: {args.first_name} {args.last_name}")
    print(f"Address: {args.street}, {args.city}, {args.state}")

if __name__ == "__main__":
    main()
