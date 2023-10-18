# soda_api 
<h2>PROJECT OVERVIEW</h2>
<p> this is a simple api endpoint for soda lovers to use to learn about how apis work,by doing simple CRUD works<br>
 its made on django rest framework and probably will front end with react, only time will tell
 haha</p>
 <ul>
  <li><img style="width:50%;" src="https://github.com/bedah-kym/soda_api/assets/85731257/5b8f371e-b759-47ca-b3a7-d4801175dc90">
     <p>A robust admin interface to help you configure tokens and manage all sites actions like users and accounts</p>
  </li>
  
  <li><img  style="width:50%;" src="https://github.com/bedah-kym/soda_api/assets/85731257/1867cda9-d6f1-4a6d-bef9-2b944418d880">
   <p>The main interface is the default django rest framework ui , good for checking everything out ie products and you can also GET POST PATCH or DELETE items through the forms provided.<br>
   the ui also has links to the product details url and awesome pagination</p>
  </li>
  <img  style="width:50%;"src="https://github.com/bedah-kym/soda_api/assets/85731257/8ba9a15d-04c1-404b-a685-0c18f3f9d42c">
  <img  style="width:50%;"src="https://github.com/bedah-kym/soda_api/assets/85731257/f4e61dde-dcaa-4c91-8bab-6bc70674dec5">
  <img  style="width:50%;"src="https://github.com/bedah-kym/soda_api/assets/85731257/6d2ce8ad-7d28-46a2-af0e-802f50bde9a5">
 
 </ul>
 <h2>USAGE AND INSTALLATION</h2>
 <h4> how to run it in your local machine</h4>
 <p>
  <li>create a folder for the project then using powershell or cmd cd into the folder then clone the repository inside the project folder</li>
  <li>after you clone the repo, create a virtual environment using pipenv or venv.</li>
  <li> after activating the virtual environment cd into drinks/ and run <code>pip install -r requirements.txt</code>  </li>
  <li>with all  the requirements installed <code>run python manage.py runserver</code></li>
  <li> if you get <code> unapplied migrations error</code> stop the server using ctrl c </li>
  <li>apply neccesarry migrations using <code>python manage.py migrate</code></li>
  <li>create superuser <code>python manage.py create superuser</code> this will be your admin </li>
  <li>use the admin to create a new user to test out the site,also make sure to add new stuff to the database</li>
 </p>
 <h3>under developmnet</h3>
 <p> while exploring django all-auth i decided it would be great to add user authentication through social platforms 
 instead of using a website to get auth tokens.Goal is when done you can use your custom drinks api to allow your friends to querry or add stuff</p>
 <p> The consumer app has premade code which acts as a consumer/client which you can use to access the api via terminal.<br>
  this project is still under development, so if something dosent work or you want to contribute jus do it and ill pull it.
  if you want to imporve this read me also please do. Thank  you
  <blockquote>DISCLAIMER  this is not a lib so am assuming you know or are learning django as this project might be tricky for noobs to run, if your are learning django rest i reccommend you check out the code to customise it to your usage parameters(you can change the models from soda drinks to say pets or cars) just make sure to run <code>python manange.py makemigrations</code> after you save the models.py file</blockquote>
 </p>
 <h3>FUTURE CHANGES</h3>
 i want to make it general porpose so you could use it as a package and connect it to a service like an e-commerce website instead of writing an api from scratch. 
