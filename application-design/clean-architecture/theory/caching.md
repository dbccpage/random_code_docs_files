# Caching

### **Caching Layer**

#### **Purpose:**

* Improves **application performance** by reducing database queries.
* Stores frequently accessed data **in-memory** using **Redis, MemoryCache, or a distributed cache**.
* Ensures faster responses for **read-heavy applications**.

#### **Components:**

* **In-Memory Cache** (MemoryCache, Redis).
* **Cache Invalidations** (TTL, Evictions).
* **Distributed Caching** (Cloud-based caching services).

#### **Example in C#:**

**Using MemoryCache**

```csharp
csharpCopyEditpublic class CachedUserRepository : IUserRepository
{
    private readonly IMemoryCache _cache;
    private readonly IUserRepository _innerRepository;

    public CachedUserRepository(IMemoryCache cache, IUserRepository innerRepository)
    {
        _cache = cache;
        _innerRepository = innerRepository;
    }

    public async Task<User> GetUserByIdAsync(int id)
    {
        return await _cache.GetOrCreateAsync($"User_{id}", async entry =>
        {
            entry.AbsoluteExpirationRelativeToNow = TimeSpan.FromMinutes(10);
            return await _innerRepository.GetUserByIdAsync(id);
        });
    }
}
```

* This ensures **cached results** are used before querying the database.
