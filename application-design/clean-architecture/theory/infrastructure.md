# Infrastructure

### **Infrastructure Layer**

#### **Purpose:**

* Contains **implementation details** of the system, including:
  * **Data persistence (EF Core, Dapper, ADO.NET)**
  * **External services (SMTP, HTTP clients, message queues)**
  * **Third-party integrations (e.g., Stripe, Twilio)**
* Houses **repository implementations**, **email services**, and **configuration settings**.

#### **Components:**

* **Repositories** (Implements Core Contracts)
* **EF Core DbContext** (or another ORM)
* **External API Clients**
* **Logging & Caching Services**

#### **Example in C#:**

**EF Core DbContext (Infrastructure Layer)**

```csharp
csharpCopyEditpublic class ApplicationDbContext : DbContext
{
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
        : base(options) { }

    public DbSet<User> Users { get; set; }
}
```

* The **ApplicationDbContext** handles **database interactions** but remains in the **Infrastructure Layer** to separate it from business logic.
