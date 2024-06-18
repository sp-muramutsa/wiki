## PROJECT OVERVIEW
This project implements a Wiki encyclopedia using Python, HTML, and CSS. The application allows users to view, search, create, edit, and navigate through encyclopedia entries.

## IMPLEMENTATION DETAILS
1. **Backend Logic**: Utilizes Python to manage the content and routing of encyclopedia entries.
2. **Frontend**: Uses HTML and CSS for structuring and styling the web pages.
3. **Markdown to HTML Conversion**: Uses the `markdown2` package to convert Markdown content to HTML for display.

## FEATURES

1. **Entry Page**
   - Visiting `/wiki/TITLE`, where `TITLE` is the title of an encyclopedia entry, renders a page displaying the contents of the entry.
   - If an entry does not exist, an error page is displayed.
   - The title of the page includes the name of the entry.

2. **Index Page**
   - `index.html` lists all encyclopedia entries as clickable links that direct the user to the respective entry page.

3. **Search**
   - Users can search for encyclopedia entries using a search box in the sidebar.
   - If the query matches an entry name, the user is redirected to that entry’s page.
   - If the query does not match exactly, a search results page displays all entries that contain the query as a substring.
   - Clicking on any entry name in the search results takes the user to that entry’s page.

4. **New Page**
   - Clicking “Create New Page” in the sidebar directs the user to a page where they can create a new entry.
   - Users can enter a title and Markdown content for the new page.
   - Clicking the save button saves the new entry, unless an entry with the same title already exists, in which case an error message is displayed.
   - Upon successful creation, the user is redirected to the new entry’s page.

5. **Edit Page**
   - Each entry page includes a link to edit the entry.
   - The edit page pre-populates a textarea with the existing Markdown content.
   - Users can save changes made to the entry, and upon saving, are redirected back to the entry’s page.

6. **Random Page**
   - Clicking “Random Page” in the sidebar takes the user to a random encyclopedia entry.

7. **Markdown to HTML Conversion**
   - Converts Markdown content to HTML before displaying it on each entry’s page.
   - Uses the `markdown2` package for the conversion.

