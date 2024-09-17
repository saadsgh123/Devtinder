# DevTinder

## Introduction
DevTinder is a full-stack web application designed to help developers build and showcase their portfolios, while allowing employers to easily discover and connect with talent. Developers can create profiles by entering their personal information, skills, and projects, along with uploading photos and links to their work. Employers can search for developers based on specific criteria and view detailed profiles to assess their qualifications. The platform serves as both a portfolio builder for developers and a recruitment tool for employers, providing a streamlined way for both parties to connect.
## Introduction: Inspiration Behind DevTinder

DevTinder started as a passion project for a group of developers who wanted to solve a simple but crucial problem: helping developers showcase their skills and projects in a way that's easy for employers to find and evaluate. We envisioned a platform where developers could highlight their achievements and recruiters could find the talent they need.

Our inspiration came from seeing how difficult it was to stand out in the sea of applicants on traditional platforms like LinkedIn. We wanted to create a space that truly put developers' work and portfolios front and center, showcasing their projects in a visually appealing and functional way.

## Problem We Set Out to Solve

We realized that while LinkedIn and other platforms give developers space to list their skills, they don't always allow for showcasing projects dynamically. So, our main goal was to build a portfolio-based platform where users can easily upload their work, display projects, and highlight their technical abilities.

### The Challenges

While we had the vision, bringing it to life was a technical challenge. Some of the hurdles we faced included:
- **Database Design:** Structuring the database to support dynamic portfolio updates and search functionalities.
- **Responsive Design:** Ensuring that DevTinder looks great across devices was harder than expected. We struggled with CSS breakpoints and responsiveness, but eventually found solutions through grid and flexbox layouts.
- **Image Upload and Display:** Handling media uploads in a way that’s secure and scalable took time to figure out.

However, these challenges helped us grow as developers, and we learned a lot through trial and error.

## Technical Details

DevTinder is built using a combination of **HTML/CSS** for the frontend and **Python** for the backend. Here are some of the key technical decisions and why we chose them:

### 1. Backend: Flask and SQLAlchemy
We chose **Flask** as our backend framework because of its simplicity and flexibility. We paired it with **SQLAlchemy** to manage our database operations. This allowed us to:
- Easily define our models for `Developers` and `PortfolioItems`.
- Quickly integrate MySQL for handling the storage of user data and portfolio entries.

### 2. Dynamic Form Handling
To enable developers to update their portfolios in real-time, we created an interactive form that sends AJAX requests to our API. This ensures that changes can be made without reloading the page, giving the user a smooth experience.

### 3. Frontend: HTML, CSS, and Bootstrap
We opted for **Bootstrap** in combination with **custom CSS** to handle the layout and styling. Bootstrap gave us a solid foundation for responsive design, which was one of our major pain points.


## Features We're Proud Of

- **Dynamic Portfolios**: Developers can create and edit their portfolios, showcasing their projects with images and descriptions.
- **Search Functionality**: Employers can search for developers based on skills and projects, making it easier for them to find the right fit.
- **Responsive Design**: DevTinder works seamlessly across different screen sizes, making it accessible to anyone on any device.


## Screenshots

Here's a look at DevTinder in action!

![Homepage](path/to/homepage.png) ta tzid a saad tsawer hna if you could me design ghaliban wla ta mn site live labghiti

![Developer Profile](path/to/developer_profile.png)

![Project Entry Form](path/to/project_form.png)

## Next Iterations and Future Plans

We have a lot of ideas for the next iteration of DevTinder. Some features we plan to implement include:

## Deployed Site
[DevTinder](http://zoubjd.tech)

## Blog Link
[Medium Blog](https://medium.com/...)

## Our LinkedIn Profiles
- **Zouhair**: [Zouhair Bajdouri](https://www.linkedin.com/in/zouhair-bajdouri-5a33a5280/)
- **Saad**: *(LinkedIn link to be added)*
- **Badr**: *(LinkedIn link to be added)*

## Installation

To install the necessary dependencies for DevTinder, use the following commands:

```bash
# Install Flask
pip install Flask

# Install WTForms
pip install WTForms

# Install MySQLdb
pip install mysqlclient

# Install SQLAlchemy
pip install SQLAlchemy
```
## Usage
```bash
# Clone the repository:
git clone https://github.com/your-repo/devtinder.git

# Navigate to the project directory:
cd devtinder

# Run the project:
python3 run.py

```

## Contributing

Each team member worked on specific parts of the project while helping each other as needed. Contributions to the project are welcome, and we encourage collaboration to improve DevTinder.

## Related projects

The most closely related projects are:

[LinkedIn](https://www.linkedin.com/)
[Tinder](https://tinder.com/)

These platforms inspired the concept behind DevTinder, combining professional networking with easy-to-use portfolio creation.

## licensing
??

## Final Thoughts

DevTinder represents our growth as developers, both in technical skills and teamwork. We've learned that building a project is as much about overcoming challenges as it is about writing code. We hope that as you explore DevTinder, you'll not only see a functional application but also the creativity and passion that went into building it.

This is only the beginning, and we're excited about what comes next.

🚀 Happy Coding!
