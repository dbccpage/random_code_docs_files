# Junk - Notes

1. Read the File
   1. Load file contents.      \
      \
      🔹 2. Extract Structural Components      \
      ✅ Namespace & Classes (Inheritance & Implemented Interfaces), Methods, MethodCalls, Forms, SqlQueryCalls, UIControls, EventHandlers      \
      ✅

🔹 3. Find Database Calls\
✅ ORM Calls (Entity Framework, Dapper, LINQ, Hibernate, etc.)\
\- Currently, I am finding ADO and ODBC calls and all SQL Server stored procedure calls if directly refernced in VB.NET and/or JS

🔹 4. Identify UI Forms

🔹 5. Find Functions & Methods\
✅ Method Definitions\
✅ Static Initializers & Constructors\
✅ Method Calls (Cross-file references)\
✅ Lambda Functions & Anonymous Methods (not implemented specfically)...this is part of later static analysis. I am trying to yank all the data to markdown and Mongo(?). Other\
services from my other applications in Cortex will grab data according to events and messaging/orchestration between Atlas and other applications

🔹 6. Detect UI Components & Event Handlers (not implemented as yet...just bulk data scraping)\
✅ Event-Driven Code (Handles Click, @OnClick, etc.)\
✅ UI Control Declarations (Button, TextBox, DropDown, etc.)\
✅ XAML/WPF/Blazor Component Analysis (if applicable)

Key Refactoring Concepts\
Modular Services:\
Create individual services such as:

FormAnalyzer: Extracts forms, controls, and event handlers from UI files.\
SourceCodeParser: Extracts classes, methods, and method calls from code files.\
DatabaseCallExtractor: Splits into (a) one for stored procedure/command-based calls and (b) one for literal SQL query extraction.\
Clear Workflow:\
The FileAnalyzer should loop through files, detect their type (using file extensions), and then delegate parsing accordingly:

For VB UI files (e.g., \*.vb forms, \*.aspx, \*.ascx), call the FormAnalyzer.\
For other code files, call the SourceCodeParser and DatabaseCallExtractor services.\
Unified Output Structure:\
Each service returns a standardized dictionary or domain object (e.g., a ParserConfig) with keys for classes, methods, event handlers, and database calls.\
FileAnalyzer then aggregates these into its master collections: forms, code\_flows, and all\_code\_files.
