# Silva Framework Documentation

**Silva Framework** is a 100% Brazilian project born out of the need to simplify web development in Python. The idea emerged during a period of extreme exhaustion, amidst burnout, when I realized that the most popular web frameworks in Python, although very good, are often complex and difficult to use efficiently. On the other hand, lesser-known frameworks lack support and robustness, making them difficult to use in production.

The goal of the **Silva Framework** is to provide a simpler, faster, and more practical solution for web application development in Python, while maintaining the efficiency and flexibility needed to compete with modern JavaScript frameworks. Over time, I’ve been refining and updating the project with love and dedication, as I believe it can help make web development more accessible and agile for Python developers.

This framework is designed to be intuitive and easy to integrate, aiming to provide developers with a powerful tool without overwhelming them with unnecessary complexity. Although the project is still under development, the plan is to keep improving and expanding its features to provide the best possible experience for the Python community.

---

### Project Objectives

- **Simplicity**: Make it easier to create web applications in Python without the need to deal with complex configurations or excessive libraries.
- **Performance**: Focus on creating a fast and lightweight framework, suitable for both small projects and large-scale applications.
- **Robustness**: Ensure the framework is resilient, flexible, and well-structured, with a focus on meeting common production requirements.
- **Continuous Updates**: The team (me) is constantly improving the framework, with a focus on community feedback and the evolution of the Python ecosystem.

---


### Future Vision

With the **Silva Framework**, the goal is to provide a solid solution that can compete healthily with JavaScript frameworks, but with the practicality and style of Python. Future improvements will include better support for database integration, performance optimizations, and new features to further facilitate development.

I thank everyone who is following and contributing to the growth of the project. If you have suggestions or want to contribute, feel free to open an issue or pull request. Collaboration is always welcome!

### Initial Structure

```bash
silva-framework/
├── silva/                    # Main directory of the framework
│   ├── __init__.py           # Package initialization
│   ├── core/                 # Core logic of the framework
│   │   ├── app.py            # Main file that initializes the framework
│   │   ├── server.py         # HTTP server implementation
│   │   └── middleware.py     # Middleware (authentication, logging, etc.)
│   ├── router/               # Routing module
│   │   └── router.py         # Routing logic
│   ├── views/                # Logic for rendering views/templates
│   │   └── views.py          # View rendering logic
│   ├── utils/                # General utilities
│   │   └── utils.py          # Helper functions
├── examples/                 # Usage examples
│   └── basic_app.py          # Basic app example using the framework
├── tests/                    # Test directory
│   ├── core/                 # Tests for core logic
│   │   ├── test_server.py    # Tests for the HTTP server
│   │   └── test_middleware.py # Tests for middleware
│   ├── router/               # Tests for routing
│   │   └── test_router.py    # Tests for the router
│   ├── views/                # Tests for views
│   │   └── test_views.py     # Tests for views
├── .gitignore                # Git ignore file
├── requirements.txt          # Project dependencies
├── README.md                 # Framework documentation
└── setup.py                  # Framework installation script
```

### Description of Files

```bash

silva/app.py: The main file that initializes the framework. It can configure the server, routing, and middleware management.

silva/router.py: Responsible for handling HTTP request routing, such as defining routes and associating functions to endpoints.

silva/server.py: The web server implementation. It may use asyncio or any other library to create the HTTP server. It can also provide integration with WSGI or ASGI, depending on your choice.

silva/views.py: Handles the rendering of views, such as HTML or templates, for server responses.

silva/middleware.py: This is where you can implement intermediate functionality, such as authentication, permission checks, or logging.

silva/utils.py: Helper functions for common operations that the framework may need, such as string or date manipulation.

tests/: Directory for unit and integration tests, which is essential to ensure the framework behaves as expected.

examples/: Examples of how to use the framework. This directory provides practical use cases for developers.

requirements.txt: Dependency file. You can start with the libraries needed for the framework, such as asyncio, jinja2 (if you use HTML templates), etc.

setup.py: Script that allows you to install the framework as a Python package.
```

# Python Version

```bash 
^3.12
````