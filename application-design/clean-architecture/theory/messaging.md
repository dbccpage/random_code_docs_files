# Messaging

### **Messaging Layer (Event-Driven Architecture)**

#### **Purpose:**

* Enables **asynchronous communication** between components using **event-driven architecture**.
* Implements **message queues (RabbitMQ, Kafka, Azure Service Bus)** to decouple services.
* Allows **scalability** in microservices or distributed systems.

#### **Components:**

* **Message Queues** (RabbitMQ, Azure Service Bus, Kafka).
* **Event Handlers** – Process incoming messages asynchronously.
* **Publishers & Subscribers** – Send and receive events.

#### **Example in C#:**

**Event Publisher**

```csharp
csharpCopyEditpublic class UserRegisteredEvent
{
    public int UserId { get; set; }
    public string Email { get; set; }
}

public interface IMessageBus
{
    void Publish<T>(T message);
}

public class RabbitMQMessageBus : IMessageBus
{
    public void Publish<T>(T message)
    {
        var json = JsonConvert.SerializeObject(message);
        // Publish to RabbitMQ (omitting actual connection details)
    }
}
```

* **Event publishers** notify subscribers about changes (e.g., `UserRegisteredEvent`).

**Event Subscriber**

```csharp
csharpCopyEditpublic class UserRegisteredEventHandler
{
    private readonly IEmailService _emailService;

    public UserRegisteredEventHandler(IEmailService emailService)
    {
        _emailService = emailService;
    }

    public void Handle(UserRegisteredEvent userEvent)
    {
        _emailService.SendWelcomeEmail(userEvent.Email);
    }
}
```

* **Subscribers process events asynchronously**, improving system decoupling.
