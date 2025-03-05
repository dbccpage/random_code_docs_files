# Functional Calling

```csharp
// Entity Framework Approach
public class UserRepository 
{
    private readonly DbContext _context;

    public List<User> GetActiveUsers()
    {
        return _context.Users
            .Where(u => u.IsActive)
            .ToList();
    }
}

// Functional SQL Approach
public class UserOperations
{
    private Func<DbConnection, List<User>> GetUsers;
    private Func<List<User>, List<User>> FilterActiveUsers;

    public List<User> ProcessUsers(DbConnection connection)
    {
        return FilterActiveUsers(
            GetUsers(connection)
        );
    }
}
```

{% embed url="https://arxiv.org/html/2502.00032v1" %}



{% embed url="https://youtu.be/Hw6O76Oq9oQ?si=7C_TFRJ9axVL_j-0" %}
