# Adapters

### **Adapter Layer (Interface Adapters)**

#### **Purpose:**

* Acts as a bridge between the **core application logic (Use Cases)** and **external systems** (e.g., UI, APIs, Databases).
* Converts data formats between **external layers** (e.g., controllers, APIs, UI) and the **application core**.

#### **Components:**

* **Controllers** (e.g., Web API or MVC Controllers)
* **View Models** (DTOs)
* **Presenters & Mappers** (Convert entities to DTOs and vice versa)

#### **Example in C#:**

```csharp
csharpCopyEdit[ApiController]
[Route("api/[controller]")]
public class UsersController : ControllerBase
{
    private readonly IUserService _userService;

    public UsersController(IUserService userService)
    {
        _userService = userService;
    }

    [HttpGet("{id}")]
    public async Task<IActionResult> GetUser(int id)
    {
        var user = await _userService.GetUserByIdAsync(id);
        if (user == null)
            return NotFound();

        return Ok(user);
    }
}
```

* Here, **UsersController** is an **adapter** between HTTP requests and **business logic**.
