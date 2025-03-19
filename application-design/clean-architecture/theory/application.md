# Application

### **Application Layer (Use Cases)**

#### **Purpose:**

* Serves as the **entry point** for business logic.
* Implements **application-specific rules** (e.g., business workflows).
* **Orchestrates interactions** between domain entities and external components (repositories, services, etc.).
* Exposes services via **commands and queries** (often using **CQRS**).

#### **Components:**

* **Use Cases (Application Services)** – Handles business operations.
* **DTOs (Data Transfer Objects)** – Represents data structures for input/output.
* **MediatR Handlers (Optional)** – Uses **CQRS pattern** for separating queries and commands.

#### **Example in C#:**

**Use Case (Application Layer)**

```csharp
csharpCopyEditpublic class GetUserByIdHandler : IRequestHandler<GetUserByIdQuery, UserDto>
{
    private readonly IUserRepository _userRepository;

    public GetUserByIdHandler(IUserRepository userRepository)
    {
        _userRepository = userRepository;
    }

    public async Task<UserDto> Handle(GetUserByIdQuery request, CancellationToken cancellationToken)
    {
        var user = await _userRepository.GetUserByIdAsync(request.Id);
        if (user == null)
            return null;

        return new UserDto
        {
            Id = user.Id,
            Name = user.Name,
            Email = user.Email
        };
    }
}
```

* The **Application Layer** ensures that core business logic is separated from controllers and repositories.
* **Commands & Queries** help implement **CQRS (Command Query Responsibility Segregation)**.
