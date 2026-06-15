classDiagram
    class Customer_Info {
        -String name
        -List~Transaction_Info~ purchaseHistory
        +isVerifiedUser() bool
        +addPurchase(Transaction_Info) void
    }

    class Mechandise_Info {
        -String name
        -float price
        -String category
        -float popularityRating
        +getPrice() float
    }

    class Order_Info {
        -List~Mechandise_Info~ items
        +addItem(Mechandise_Info) void
        +filterByCategory(String) List~Mechandise_Info~
        +getAllItems() List~Mechandise_Info~
    }

    class Transaction_Info {
        -List~Mechandise_Info~ selectedItems
        +addItem(Mechandise_Info) void
        +computeTotal() float
    }

    Order_Info o-- "many" Mechandise_Info : catalogs
    Transaction_Info o-- "1..*" Mechandise_Info : contains
    Customer_Info "1" --> "many" Transaction_Info : has history