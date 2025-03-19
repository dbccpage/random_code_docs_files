# Logging & Monitoring

### **Logging & Monitoring Layer**

#### **Purpose:**

* Tracks **application health**, errors, and performance metrics.
* Collects logs from **API requests, exceptions, background jobs**.
* Uses tools like **Serilog, ELK Stack (Elasticsearch, Logstash, Kibana), Application Insights**.

#### **Components:**

* **Structured Logging** (Serilog, NLog, log4net).
* **Monitoring & Metrics** (Prometheus, Grafana, Azure App Insights).
* **Distributed Tracing** (OpenTelemetry, Jaeger).

#### **Example in C#:**

**Serilog Configuration**

```csharp
csharpCopyEditLog.Logger = new LoggerConfiguration()
    .WriteTo.Console()
    .WriteTo.File("logs/app.log", rollingInterval: RollingInterval.Day)
    .WriteTo.Seq("http://localhost:5341")
    .CreateLogger();
```

* This logs events to the console, a file, and a remote log server (Seq).

**Logging an Exception**

```csharp
csharpCopyEdittry
{
    throw new Exception("Something went wrong!");
}
catch (Exception ex)
{
    Log.Error(ex, "An error occurred while processing the request");
}
```

* **Structured logging** helps diagnose issues quickly.
