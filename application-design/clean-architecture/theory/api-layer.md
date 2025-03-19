# API Layer

### **API Layer (External API Gateway)**

#### **Purpose:**

* Acts as a **public-facing** layer that handles HTTP requests and API security.
* Implements **API versioning**, **rate-limiting**, and **authentication**.
* **Separates API concerns** from UI (MVC) or microservices.

#### **Components:**

* **API Controllers** – Handle HTTP requests.
* **Middleware** – Logging, security, rate-limiting.
* **Authentication & Authorization** – JWT, OAuth, API Keys.
* **API Versioning** – Supports multiple versions (`v1`, `v2`).
* **Swagger/OpenAPI** – Documents API endpoints.

#### **Example in C#:**

**API Controller**

```csharp
csharpCopyEdit[ApiController]
[Route("api/v1/users")]
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
        if (user == null) return NotFound();

        return Ok(user);
    }
}
```
