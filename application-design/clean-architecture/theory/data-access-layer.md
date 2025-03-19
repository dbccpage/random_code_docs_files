# Data Access Layer

### **Data Access Layer (DAL)**

#### **Purpose:**

* Serves as a **lower-level implementation** of data persistence.
* Typically includes **ORM configurations**, **raw SQL queries**, or **direct data manipulation** mechanisms.
* **Optional** in Clean Architecture if using repositories.

#### **Components:**

* **Entity Framework Core Configurations**
* **Migrations and Seed Data**
* **Dapper Queries (if needed for performance)**

#### **Example in C#:**

**Data Access Using Dapper (In Infrastructure)**

```csharp
csharpCopyEditpublic class UserRepository : IUserRepository
{
    private readonly IDbConnection _db;

    public UserRepository(IDbConnection db)
    {
        _db = db;
    }

    public async Task<User> GetUserByIdAsync(int id)
    {
        var sql = "SELECT * FROM Users WHERE Id = @Id";
        return await _db.QuerySingleOrDefaultAsync<User>(sql, new { Id = id });
    }
}
```

* The **DAL** can **optimize performance** by **using raw SQL** with **Dapper** instead of Entity Framework for read-heavy operations.
