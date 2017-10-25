//require the routes so that we have access to campgronds and comments

var Campground = require("../models/campground");
var Comment = require("../models/comment");

// all the middleare functions are defined in this object
var middlewareObj = {};

middlewareObj.checkCampgroundOwnership = function(req, res, next) {
 if(req.isAuthenticated()){
        Campground.findById(req.params.id, function(err, foundCampground){
           if(err){
               res.redirect("back");
           }  else {
               // does user own the campground?
            if(foundCampground.author.id.equals(req.user._id)) {//if the person logged in is the same as the person who created the camoground
                next();
            } else {
                res.redirect("back");
            }
           }
        });
    } else {
        req.flash("error", "You dont have permission to do that");
        res.redirect("back");
    }
}

middlewareObj.checkCommentOwnership = function(req, res, next) {
 if(req.isAuthenticated()){
     //when authorised find the campground
        //if the user and author are the same then proceed to callback function'
        //else go back to previous page
        Comment.findById(req.params.comment_id, function(err, foundComment){
           if(err){
               res.redirect("back");
           }  else {
               // does user own the comment?
            if(foundComment.author.id.equals(req.user._id)) {
                next();
            } else {
                req.flash("error", "You dont have permission to do that");
                res.redirect("back");
            }
           }
        });
    } else {
        req.flash("error", "You need to be logged in to do that");
        res.redirect("back");
    }
}

middlewareObj.isLoggedIn = function(req, res, next){
    if(req.isAuthenticated()){
        return next();
    }
    //executed only when the callback function is executed-next page-do it before redirect
    //accessing this on the next request
    else{
        req.flash("error", "You need to be logged in to that");
        res.redirect("/login");
        
    }
}

module.exports = middlewareObj;