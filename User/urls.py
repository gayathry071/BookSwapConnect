from django.urls import path
from User import views
app_name="User"
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    
    path('UserAddBook/',views.UserAddBook,name="UserAddBook"),
    path('UserBookDel/<int:id>',views.UserBookDelete,name="UserBookDel"),
    path('UserBookUpdate/<int:eid>',views.UserBookupdate,name="UserBookUpdate"),

    path('Search/',views.searchbook,name="Search"),

    path('Ajaxsearch/',views.ajaxsearch,name="Ajaxsearch"),

    path('Viewmore/<int:bid>',views.Viewmore,name="Viewmore"),


    path('Swaprequest/<int:bid>',views.Swaprequest,name="Swaprequest"), 
    path('Viewrequest/',views.Viewrequest,name="Viewrequest"),
    path('Viewbooks/<int:Fromid>/<int:sid>',views.Viewbooks,name="Viewbooks"),

    path('Acceptbook/<int:bid>/<int:sid>',views.Acceptbook,name="Acceptbook"),
    path('Rejectedbook/<int:bid>/<int:rid>',views.Rejectedbook,name="Rejectedbook"),

    path('payment/<int:amt>/<int:sid>',views.payment,name="payment"),

    path('mybooking/',views.mybooking,name="mybooking"),
    path('view_publisher_book/',views.view_publisher_book,name="view_publisher_book"),

    path('usercomplaint/',views.usercomplaint,name="usercomplaint"),

    path('Viewcomplaints/',views.Viewcomplaints,name="Viewcomplaints"),

     path('Searchpbook/',views.searchpbook,name="searchpbook"),

    path('Ajaxpsearch/',views.ajaxpsearch,name="ajaxpsearch"),

    path('ViewPmore/<int:bid>',views.ViewPmore,name="ViewPmore"),

    path('Addcart/<int:pid>',views.Addcart,name="Addcart"),
    
    
    path('Mycart/',views.Mycart,name="Mycart"),
    path('DelCart/<int:did>',views.DelCart,name="DelCart"),
    path('CartQty/',views.CartQty,name="CartQty"),

    path('cartpayment/',views.cartpayment,name="cartpayment"),
    path('loader/',views.loader,name="loader"),
    path('paymentsuc/',views.paymentsuc,name="paymentsuc"),

    path('mypdtbooking/',views.mypdtbooking,name="mypdtbooking"),
    path('mypublisherbook/<int:id>',views.mypublisherbook,name="mypublisherbook"),

    path('rating/<int:mid>',views.rating,name="rating"),  
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),

    path('userrating/<int:mid>',views.userrating,name="userrating"),  
    path('userajaxstar/',views.userajaxstar,name="userajaxstar"),

    path('viewuser/<int:id>',views.viewuser,name="viewuser"),
    
    
    
    path('MyGenre/',views.MyGenre,name="MyGenre"),


    path('GenreDel/<int:id>',views.GenreDel,name="GenreDel"),
   
    path('MyWishList/<int:id>',views.MyWishList,name="MyWishList"),

    path('ViewWishList/',views.ViewWishList,name="ViewWishList"),

    path('WishlistDel/<int:id>',views.WishlistDel,name="WishlistDel"),

    #user Booking

    
    path('AddcartUser/<int:pid>',views.AddcartUser,name="AddcartUser"),
    
    
    path('MycartUser/',views.MycartUser,name="MycartUser"),
    path('DelCartUser/<int:did>',views.DelCartUser,name="DelCartUser"),

    path('cartpaymentUser/',views.cartpaymentUser,name="cartpaymentUser"),



    path('vieworders/',views.vieworders,name="vieworders"),

    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),

    path('ViewUserBuyProduct/<int:id>',views.ViewUserBuyProduct,name="ViewUserBuyProduct"),

    path('swappayment/<int:id>',views.swappayment,name="swappayment"),

    path('publisherbook_review/<int:id>',views.publisherbook_review,name="publisherbook_review"),






    path('logout/',views.logout,name="logout"),


]
