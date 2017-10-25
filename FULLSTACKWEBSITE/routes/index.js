var express = require("express");
var router = express.Router();
var passport = require("passport");
var User=require("../models/user");


//root route
router.get("/", function(req, res){
    res.render("landing");
});


//AUTH ROUTES
//we use the same passport.authenticate but in different ways

//register routes
router.get("/register",function(req,res){
    res.render("register");
});

router.post("/register",function(req,res){
    var newUser = new User({username:req.body.username});
    User.register(newUser,req.body.password,function(err,user){
        if(err){
            console.log(err);
            return res.render("/register"); //return goes back to the call back
        }
        passport.authenticate("local")(req,res,function(){
            res.redirect("/campgrounds");
        });
    });
});

//login routes
router.get("/login",function(req,res){
    res.render("login");
});

//when input is submitted
router.post("/login",passport.authenticate("local",{//middleware
    successRedirect:"/campgrounds",
    failureRedirect:"/login"
}),function(req,res){
    req.flash("success", "You are logged in");
});

//logout
router.get("/logout",function(req,res){
    req.logout();
    req.flash("success", "Logged you out!");
    res.redirect("/campgrounds");
});

//middleware

function isLoggedIn(req,res,next){
    if(req.isAuthenticated()){
        return next();
    }
    res.redirect("/login");
}

module.exports=router;
