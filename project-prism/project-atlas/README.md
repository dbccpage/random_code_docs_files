# Project Atlas

### 1. **Initialization**

#### **Configuration & Environment Setup**

* **Configuration Loading:**
  * Reads configuration from a `config.json` file.
  * Validates configuration file existence, accessibility, and directory paths.
* **Infrastructure Initialization:**
  * **Logger:** A central logging service to record information, errors, and debugging details.
  * **ConnectionManager:** Builds and manages database connection strings based on configuration settings.
  * **Database Settings:**
    * Reads server, database, authentication type (Windows or SQL), username, and password.
    * Validates credentials and builds the appropriate connection string.

#### **Core Service Initialization**

* **DbContext Initialization:**
  * `SqlServerDbContext` is created to manage direct call/response interactions with SQL Server.
* **Repository & Adapter Setup:**
  * `SqlServerAdapter` and `SqlServerRepository` are configured to abstract database interactions.
* **Documentation Services:**
  * Several documentation services are initialized:
    * **DatabaseDocumentationService:** For generating documentation of database objects.
    * **ProgrammabilityDocumentationService & SchemaDocumentationService:** (if applicable) for further database details.
    * **SourceFileDocumentationService:** To generate documentation (Markdown) for source code files.
* **Additional Core Services:**
  * **CodeKnowledgeService:** Processes analysis results, generates quality reports, and saves knowledge graphs.
  * **CodeInsightCoordinator:** Coordinates advanced code insight processes.
  * **IntegratedParserService:** Handles integrated parsing across various file types.

***

### 2. **File Analysis Phase**

#### **File Scanning and Parsing**

* **Supported File Types:**
  * The system supports various file extensions (e.g., `.vb`, `.cs`, `.aspx`, `.ascx`, `.razor`, etc.), determined by the `FileType` module.
* **Analyzing UI Forms:**
  * **FileAnalyzer** scans for VB and UI files.
  * For each file (e.g., VB forms, ASPX pages), it:
    * Extracts form information (class name, controls, event handlers).
    * Registers forms with the `FormDocumentationRegistry`.
    * Maps event handlers and method calls to create **code flow** entries.
* **Analyzing Code Files:**
  * The FileAnalyzer recursively scans project directories for all supported file types.
  * For each code file, it:
    * Uses the **SourceCodeParser** service to extract classes, methods, and database interactions.
    * Invokes specialized services to extract database calls:
      * **DatabaseCommandCallExtractor:** For stored procedure calls and command patterns.
      * **SQLQueryCallExtractor:** For literal SQL queries embedded in the code.
    * Aggregates results into a master collection:
      * **`_forms`:** Parsed UI form details.
      * **`_code_flows`:** Event flows and method call mappings.
      * **`_all_code_files`:** Detailed analysis results from every code file.
* **Configuration Object Population:**
  * The results are stored in a `CodeConfig` domain object, which holds forms, flows, and code file analysis.

***

### 3. **Documentation Generation Phase**

#### **Markdown and Report Generation**

* **Source Code Documentation:**
  * The **SourceFileDocumentationService** uses the aggregated code file data to create Markdown documents that catalog source files and document source code.
* **Database Documentation:**
  * The **DatabaseDocumentationService** generates documentation for database objects, stored procedures, and SQL queries.
* **Quality and Knowledge Graphs:**
  * **CodeKnowledgeService:**
    * Processes analysis results to generate a quality report.
    * Builds and saves a knowledge graph representing code dependencies and quality metrics.
  * **CodeInsightCoordinator:**
    * Further processes analysis results to provide advanced insights and visualization-ready data.
* **Output Path:**
  * All generated documentation (Markdown files, reports, knowledge graphs) are written to the configured output directory.

***

### 4. **Error Handling**

#### **Robust Error Management**

* The system has comprehensive error handling in the main execution (`Atlas.py`), including:
  * **FileNotFoundError, PermissionError, IsADirectoryError:**
    * Catches file system errors (e.g., missing or inaccessible files).
  * **OSError, UnicodeEncodeError, ValueError, MemoryError:**
    * Handles various OS-level or file encoding errors.
  * **Generic Exceptions:**
    * Logs unexpected errors with detailed stack traces.
* **Logging:**
  * Errors are logged via the central Logger service for troubleshooting and audit.

***

### 5. **Execution Flow**

#### **Main Entry Point (Atlas.py)**

* **Configuration:**
  * Atlas loads the configuration, initializes infrastructure and core services, and validates dependencies.
* **File Analysis:**
  * Calls `FileAnalyzer.analyze_project_files()` to process all project files and aggregate results.
* **Documentation Generation:**
  * Invokes documentation services to generate and write Markdown documentation.
* **Knowledge Graph & Quality Report:**
  * Processes analysis results to generate a knowledge graph and quality report.
* **Finalization:**
  * Completes execution and logs final status.
* **Exception Handling:**
  * Any errors during execution are logged with detailed tracebacks.

***

### 6. **Future Enhancements**

* **Improved Service Separation:**
  * Further refine individual services (e.g., splitting database call extraction into separate services for stored procedures vs. literal SQL queries).
* **Enhanced UI & Interactive Presentation:**
  * Consider building an interactive web or desktop app to visually present the analysis and documentation.
* **Additional File Types:**
  * Expand support for additional Microsoft-related files (e.g., `.xaml`, `.cshtml`, `.resx`) and modern frameworks.
* **Performance & Scalability:**
  * Optimize file scanning and parsing to handle larger projects with minimal latency.
