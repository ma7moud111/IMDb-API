<h1>🎬 IMDb Clone Backend API</h1>

<p>
A RESTful backend API built with <strong>Django</strong> and <strong>Django REST Framework</strong> that replicates the core functionalities of the IMDb platform. This project provides a scalable and clean backend foundation for a movie database application.
</p>

<hr />

<h2>🚀 Features</h2>

<ul>
  <li>🔐 <strong>User Authentication & Authorization</strong> (JWT-based)</li>
  <li>🎥 <strong>CRUD Operations</strong> for:
    <ul>
      <li>Movies & TV Shows</li>
      <li>Actors, Directors, Genres</li>
    </ul>
  </li>
  <li>⭐ <strong>Ratings & Reviews System</strong>
    <ul>
      <li>User-submitted reviews</li>
      <li>Automatic average rating calculation</li>
    </ul>
  </li>
  <li>🔎 <strong>Advanced Search & Filtering</strong> by title, genre, release year, rating, etc.</li>
  <li>🔗 <strong>Nested Relationships</strong> (e.g., Movies with cast and crew)</li>
  <li>🛡️ <strong>Custom Permissions</strong> (Admin vs regular users)</li>
  <li>📦 <strong>Pagination & Ordering</strong></li>
  <li>🛠️ <strong>Admin Panel</strong> via Django Admin</li>
  <li>📘 <strong>Interactive API Documentation</strong> (Swagger / Redoc)</li>
</ul>

<hr />

<h2>🧰 Tech Stack</h2>

<ul>
  <li>Python</li>
  <li>Django</li>
  <li>Django REST Framework</li>
  <li>SimpleJWT (for authentication)</li>
  <li>PostgreSQL <em>(or SQLite for development)</em></li>
  <li>drf-yasg <em>(for Swagger documentation)</em></li>
</ul>

<hr />

<h2>⚙️ Getting Started</h2>

<h3>1. Clone the repository</h3>

<pre>
<code>
git clone https://github.com/yourusername/imdb-clone-backend.git
cd imdb-clone-backend
</code>
</pre>

<h3>2. Create a virtual environment & install dependencies</h3>

<pre>
<code>
python -m venv env
source env/bin/activate  # or .\env\Scripts\activate on Windows
pip install -r requirements.txt
</code>
</pre>

<h3>3. Apply migrations</h3>

<pre>
<code>
python manage.py migrate
</code>
</pre>

<h3>4. Run the development server</h3>

<pre>
<code>
python manage.py runserver
</code>
</pre>

<h3>5. Access the API</h3>

<pre>
<code>
http://127.0.0.1:8000/api/
</code>
</pre>

<hr />
