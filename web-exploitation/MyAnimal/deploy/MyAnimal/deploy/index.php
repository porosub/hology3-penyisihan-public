<!DOCTYPE html>
<!--
TEMPLATE
Name: Zoo Planet
Version: 1.0
Created: 23 January 2014

AUTHOR
Design and code by: http://www.bootshape.com
Free stock photos by: http://www.bootshape.com

Read full license: http://www.bootshape.com/license.php

CREDITS
Background: http://subtlepatterns.com/ (extra_clean_paper)
Fonts: http://www.google.com/fonts (Actor, Duru_Sans)

SUPPORT
E-mail: bootshape.com@gmail.com
Contact: http://www.bootshape.com/contact.php
-->
<html>
  <head>
    <title>My Animal</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap -->
    <link href="css/bootstrap.css" rel="stylesheet">
    
    <!--Google Fonts-->
    <link href='http://fonts.googleapis.com/css?family=Duru+Sans|Actor' rel='stylesheet' type='text/css'>
    
    <!--Bootshape-->
    <link href="css/bootshape.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->

    <style type="text/css">
    	img.center {
  		display: block;
  		margin-left: auto;
  		margin-right: auto;
  		}
  	</style>

  </head>
  <body>
    <!-- Navigation bar -->
    <div class="navbar navbar-default navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/"><span class="green">My</span> Animal</a>
        </div>
        <nav role="navigation" class="collapse navbar-collapse navbar-right">
          <ul class="navbar-nav nav">
            <li class="active"><a href="/">Home</a></li>
            <li><a href="#">Special Offers</a></li>
            <li><a href="#">License</a></li>
            <li><a href="#">Contacts</a></li>
            <li><a href="#">Admin</a></li>
          </ul>
        </nav>
      </div>
    </div><!-- End Navigation bar -->

    <!-- Slide gallery -->
    <div class="jumbotron">
      <div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
        <!-- Indicators -->
        <ol class="carousel-indicators">
          <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>
          <li data-target="#carousel-example-generic" data-slide-to="1"></li>
          <li data-target="#carousel-example-generic" data-slide-to="2"></li>
        </ol>
        <!-- Wrapper for slides -->
        <div class="carousel-inner">
          <div class="item active">
            <img src="img/carousel1.jpg" alt="">
            <div class="carousel-caption">
            </div>
          </div>
          <div class="item">
            <img src="img/carousel2.jpg" alt="">
            <div class="carousel-caption">
            </div>
          </div>
          <div class="item">
            <img src="img/carousel3.jpg" alt="">
            <div class="carousel-caption">
            </div>
          </div>
        </div>
        <!-- Controls -->
        <a class="left carousel-control" href="#carousel-example-generic" data-slide="prev">
          <span class="glyphicon glyphicon-chevron-left"></span>
        </a>
        <a class="right carousel-control" href="#carousel-example-generic" data-slide="next">
          <span class="glyphicon glyphicon-chevron-right"></span>
        </a>
      </div>
    </div><!-- End Slide gallery -->
    <h3 class="text-center">What would you like to see?</h3>
    <!-- Thumbnails -->
    <div class="container thumbs">
      <div class="col-sm-6 col-md-4">
        <div class="thumbnail">
          <img src="img/1200px-American_Eskimo_Dog.png" alt="" class="img-circle">
          <div class="caption">
            <h3 class="text-center">Dog</h3>
            
            <div class="btn-toolbar text-center">
              <a href="/?view=dog" role="button" class="btn btn-success">View</a>
            </div>
          </div>
        </div>
      </div>
      <div class="col-sm-6 col-md-4">
        <div class="thumbnail">
          <img src="img/fox-pictures-1.png" alt="" class="img-circle">
          <div class="caption">
            <h3 class="text-center">Fox</h3>
            
            <div class="btn-toolbar text-center">
              <a href="/?view=fox" role="button" class="btn btn-success">View</a>
            </div>
          </div>
        </div>
      </div>
      <div class="col-sm-6 col-md-4">
        <div class="thumbnail">
          <img src="img/Black_white_cats.png" alt="" class="img-circle">
          <div class="caption">
            <h3 class="text-center">Cat</h3>
            
            <div class="btn-toolbar text-center">
              <a href="/?view=cat" role="button" class="btn btn-success">View</a>
            </div>
          </div>
        </div>
      </div>

      <?php
            function containsStr($str, $substr) {
                return strpos($str, $substr) !== false;
            }
	    $ext = isset($_GET["ext"]) ? $_GET["ext"] : '.php';
            if(isset($_GET['view'])) {
            	$nama = $_GET['view'];
            	//Ga boleh LFI!
            	$nama = str_replace( array( "../", "..\"" ), "", $nama );

                //Ga boleh gambar yg lain!
                if(containsStr($nama, 'dog') || containsStr($nama, 'fox') ||
                	containsStr($nama, 'cat')) {
                    echo "<h2 align=center>Here you go!.</h1>";
                    include $nama . $ext;
                } else {
                	echo "<br><br>";
                    echo "<h1 align=center>Sorry, only dog, fox,  and cat are allowed.</h1>";
                }
            }
        ?>
    </div><!-- End Thumbnails -->
    <!-- Footer -->
    <div class="footer text-center">
        <p>&copy; 2014 Zoo Planet. All Rights Reserved. Proudly created by <a class="green" href="http://bootshape.com">Bootshape.com</a></p>
    </div><!-- End Footer -->

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <!-- // <script src="https://code.jquery.com/jquery.js"></script> -->
    <script src="js/jquery.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>
    <script src="js/bootshape.js"></script>
  </body>
</html>