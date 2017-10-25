var express     = require("express"),
    app         = express(),
    bodyParser  = require("body-parser"),
    mongoose    = require("mongoose"),
    flash       = require("connect-flash"),
    passport    = require("passport"),
    LocalStrategy = require("passport-local"),
    methodOverride = require("method-override"),
    Campground  = require("./models/campground"),
    Comment     = require("./models/comment"),
    User        = require("./models/user"),
    seedDB      = require("./seeds");
    
//requiring routes
var commentRoutes    = require("./routes/comments"),
    campgroundRoutes = require("./routes/campgrounds"),
    indexRoutes      = require("./routes/index")
    
mongoose.connect("mongodb://localhost/yelp_camp_v10");
app.use(bodyParser.urlencoded({extended: true}));//we can use req.body.....-relevent for post requests
app.set("view engine", "ejs");
app.use(express.static(__dirname + "/public"));//to use the stylesheet
app.use(methodOverride("_method"));//to do a method other than get or post
// seedDB(); //seed the database
app.use(flash());

// PASSPORT CONFIGURATION
app.use(require("express-session")({//a way to require something with a function
    secret: "Once again Rusty wins cutest dog!",
    resave: false,
    saveUninitialized: false
}));
app.use(passport.initialize());
app.use(passport.session());
passport.use(new LocalStrategy(User.authenticate()));// Local is the strategy to be used
passport.serializeUser(User.serializeUser());//serialize and deserialze data when logging in
passport.deserializeUser(User.deserializeUser());

app.use(function(req, res, next){//used as global variable for the current user
    //every user has its own id assigned and can be accessed using ._id
   res.locals.currentUser = req.user;
   res.locals.error = req.flash("error");
   res.locals.success = req.flash("success");
   next();
});


//using the routes
app.use("/", indexRoutes);
app.use("/campgrounds", campgroundRoutes);
app.use("/campgrounds/:id/comments", commentRoutes);//this id can be accessed using req.params.id
//even if not mentioned in the routes

//Starting the server
app.listen(process.env.PORT, process.env.IP, function(){
   console.log("The YelpCamp Server Has Started!");
});