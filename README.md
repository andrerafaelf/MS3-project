<h1 align="center">Code Institute Website</h1>

[View the live project here.](https://the-online-post-ms3.herokuapp.com/)

This is the main website for The Online Post. It is designed to be responsibe and accessible on a range of devices, making it easy to navigate for new and existing users.

## User Experience (UX)

-   ### User stories

	- As a first time visitor I want to easily access the account creation page.
    - I want to be able to view other posts and easily create my own posts.
    - I want to edit and delete my previous posts. 
    - There needs to be a search functionality so I can filter through the various posts.
    - I want to know more about certain milestones.
    - I want to be able to give feedback to the developer.


-   ### Design
    -   #### Colour Scheme
        -   The main colours used are Black, White and Grey. 
    -   #### Typography
        -   The Works Sans font is the main font used throughout the whole website with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site correctly.

*   ### Wireframes

    -   Desktop Wireframe - [View](assets/wireframes/pcWF.png)

    -   Mobile Wireframe - [View](assets/wireframes/mobile.png)

    -   Tablet Wireframe - [View](assets/wireframes/tablet.png)

    -   Tablet Create Wireframe - [View](assets/wireframes/ipadcreate.png)

    -   Tablet Edit Wireframe - [View](assets/wireframes/tabletedit.png)

    -   Mobile Create Wireframe - [View](assets/wireframes/mobilecreate.png)

    -   Mobile Edit Wireframe - [View](assets/wireframes/mobileedit.png)

    -   Desktop Create Wireframe - [View](assets/wireframes/pccreate.png)

    -   Desktop Edit Wireframe - [View](assets/wireframes/pcedit.png)


    
## Features

-   Responsive on all device sizes

-   Interactive elements

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JS](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

1. [Materialize 1.0.0:](https://materializecss.com/about.html)
    - Materialize was used to assist with the responsiveness and styling of the website.
1. [Flask:](https://flask.palletsprojects.com/en/2.0.x/)
    - Flask was used for all the CRUD fucntionality throughout the website.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Titillium Web' font into the style.css file which is used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
    - jQuery was used along side materialize to assist in animation.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](https://github.com/andrerafaelf/MS3-project) during the design process.
1. [MongoDB:](https://www.mongodb.com/)
    - MongoDB was the selected database for this project.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/)

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    - As a first time visitor I want to easily access the account creation page.
        - This is easily accessed on the main nav bar of the page.

    - I want to be able to view other posts and easily create my own posts.
        - The main create post page is located on the main page nav bar and all posts can be found on the landing page.

    - I want to edit and delete my previous posts. 
        - After users have created their first post they can easily edit and delete their own posts in their profile page.

    - There needs to be a search functionality so I can filter through the various posts.
        - Users can filter through posts with the search functionality on the home page.

    - I want to know more about certain milestones.
        - Users have the option to apply for page moderator on the page footer, after having reached certain milestones on the website.

    - I want to be able to give feedback to the developer.
        - Any user is more than welcome to give the developer any feedback using the links in the footer.

### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone XS, iPhone 11 & iPhone 12.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs

-   On some mobile devices the category selection on the post creation page sometimes isn't accurate.
    -   Images on mobile devices are sometimes smaller than wanted.

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/andrerafaelf/MS3-project)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code

-   [Materialize](https://materializecss.com/): Materialize used throughout the project mainly to make site responsive using the Materialize Grid System.

### Content

-   All content was written by the developer.

-   Psychological properties of colours text in the README.md was found [here](http://www.colour-affects.co.uk/psychological-properties-of-colours)

### Media

-   All Images were created by the developer.

### Acknowledgements

-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.