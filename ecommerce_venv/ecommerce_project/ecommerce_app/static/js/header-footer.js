const headerTemplate = document.createElement('template');
headerTemplate.innerHTML = `

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link href='https://fonts.googleapis.com/css?family=Montserrat' rel='stylesheet'>
<style>
body{
    margin: auto;
}

.upper-header{
    
    display: flex;
    
    
    
    
    height: 40px;
    background-color: #333333;
}
.left-upper-header{
    width: 50%;
    display:flex;
    justify-content:center ;
    align-items: center;
    font-family: montserrat;
    
    

}
.right-upper-header{
    width: 30%;
    display: flex;
    justify-content:center;
    align-items: center;

    
    
}
.center-upper-header{
    width: 30%;
    display: flex;
    justify-content:center;
    align-items: center;

    
    
}
a:visited {
    color: whitesmoke;
    text-decoration: none;
}
a{
    text-decoration: none;
}
input,select {
    width: 120px;
    
    
    box-sizing: border-box;
    border: none;
    background-color: #50503e95;
    color: white;
    font-size: 15px;
  }
  .cart{
      color: aliceblue;
      background-color: aqua;
      width:150px;
      display: flex;
      justify-content:center;
      align-items: center;
      
      
  }
.main-header{
    display: flex;
    position: relative;
    height: 100px;
    background-color: rgb(255, 255, 255);
}

.left-main-header{
    display: flex;
    width: 35%;
    justify-content: center;
    align-items: center;

}
.center-main-header{
    width: 50%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: montserrat;
    

}
ul{
    display:flex;
}
.right-main-header{
    width: 15%;
    display: flex;
    justify-content:space-between;
    align-items: center;
    

}
.search{
    justify-content: center;
    align-items: center;
    
}
.searchform{
    background-color: aliceblue;
    color: black;
    width: 180px;
    height: 40px;

}
.searchbutton{
    width: 30px;
    height: 40px;
}
li{
  display: inline;
  color: gray;
  
  font-size: 12px;
  text-decoration: none;
  font-weight: bolder;
  
}
ul{
    list-style-type: none;
    
    
}

@media (max-width:768px) {
    body{
        margin: auto;
    }
    .header{
        display: block;
    }
    .upper-header{
        display: block;
        height: 150px;
        width: 100%;
        
    }
    .left-upper-header{
       
        padding-top: 20px;
        
        margin-left: auto;
        margin-right: auto
    }
        
    .center-upper-header{
        
        margin-top: 20px;
        margin-left: auto;
        margin-right: auto
        
    }
    .right-upper-header{
        
        margin-top: 20px;
        margin-left: auto;
        margin-right: auto
        
    }
    .main-header{
        display: block;
        height: 450px;
        width: 100%;
        
    }
    .left-main-header{
       
        padding-top: 20px;
        display: block;
        margin-left: auto;
        margin-right: auto
    }
        
    .center-main-header{
        
        margin-top: 20px;
        margin-left: auto;
        margin-right: auto
        
    }
    .right-main-header{
        display:block;
        margin-top: 20px;
        margin-left: auto;
        margin-right: auto;
        
        
        
    }
    span{
        margin-left: auto;
        margin-right: auto;
        display: flex;
    }
    li{
        display: block;
        margin-left: auto;
        margin-right: auto
    }
    
    .column {
        width: 100%;
        height: auto;
      }
    li{
        display: block;
        margin-left: auto;
        margin-right: auto
    }
    ul{
        display: block;
        margin-left: auto;
        margin-right: auto
    }
    
  }
 

  .center-main-header {
    overflow: hidden;
    
    
    
  }
  
  
  
  .dropdown {
    
    overflow: hidden;
    box-sizing: border-box;
  }
  
  .dropdown .dropbtn {
    font-size: 16px;  
    border: none;
    outline: none;
    
    padding: 14px 16px;
    background-color: inherit;
    font: montserrat;
    margin: 0;
    box-sizing: border-box;
  }
  
  .navbar a:hover, .dropdown:hover .dropbtn {
    background-color: aqua;
    box-sizing: border-box;
  }
  
  .dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    width: 100%;
    left: 0;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
    box-sizing: border-box;
  }
  
  
  
  .dropdown:hover .dropdown-content {
    display: block;
    box-sizing: border-box;
  }
.row{
    display: flex;
}
  
  .column {
    
    width:50%;
    padding: 10px;
    background-color: #ccc;
    height: 250px;
    text-align: center;
    
  }
  
  .column a {
    float: none;
    color: black;
    padding: 16px;
    text-decoration: none;
    display: block;
    
    margin-left: auto;
    margin-right: auto;
    
  }
  
  .column a:hover {
    background-color: #ddd;
  }
  
  
  .row:after {
    content: "";
    display: table;
    clear: both;
  }


   


   
</style>

<div class="header">
        <div class="upper-header">
            <div class="left-upper-header">
            <select name="pay-currency"  id="pay-currency" required>
                <option  disabled="true" >Currency</option>
                
                <option>GBP</option>
                <option>USD</option>
                <option>BAM</option>
            </select>
            </div>
            <div class="center-upper-header">
            <a href="#">Register</a>&nbsp&nbsp&nbsp
            
            <a href="#">Sing in</a>
            
            </div>
            <div class="right-upper-header">
                <span class="cart">
                <p>Empty</p>
                &nbsp&nbsp&nbsp
                <i style="font-size:26px" class="fa">&#xf07a;</i>
                </span>

            </div>

            
            
            

            
        </div>
        <div class="main-header">
            <div class="left-main-header">
                <b>AVENUE </b>&nbsp FASHION

            </div>
            
            <div class="center-main-header">
                
                <ul>  
                    
                    <div class="dropdown">
                        <li><button class="dropbtn">MENS
                            
                          <i class="fa fa-caret-down"></i>
                        </button></li>
                        <div class="dropdown-content">
                            
                          <div class="row">
                            <div class="column">
                              <h3>OUR LOOKBOOKS</h3>
                              <a href="#">Latest Posts</a>
                              <a href="#">Men's Lookbook</a>
                              <a href="#">Women's Lookbook</a>
                            </div>
                            <div class="column">
                              <h3>YOUR LOOKBOOK</h3>
                              <a href="#">View and Edit</a>
                              <a href="#">Share</a>
                              <a href="#">Delete</a>
                            </div>
                            
                          </div>
                        </div>
                    </div>
                    <div class="dropdown">
                        <li><button class="dropbtn">WOMENS
                            
                          <i class="fa fa-caret-down"></i>
                        </button></li>
                        <div class="dropdown-content">
                            
                          <div class="row">
                            <div class="column">
                              <h3>OUR LOOKBOOKS</h3>
                              <a href="#">Latest Posts</a>
                              <a href="#">Men's Lookbook</a>
                              <a href="#">Women's Lookbook</a>
                            </div>
                            <div class="column">
                              <h3>YOUR LOOKBOOK</h3>
                              <a href="#">View and Edit</a>
                              <a href="#">Share</a>
                              <a href="#">Delete</a>
                            </div>
                            
                          </div>
                        </div>
                    </div>
                    <div class="dropdown">
                        <li><button class="dropbtn">THE BRAND
                            
                          <i class="fa fa-caret-down"></i>
                        </button></li>
                        <div class="dropdown-content">
                            
                          <div class="row">
                            <div class="column">
                              <h3>OUR LOOKBOOKS</h3>
                              <a href="#">Latest Posts</a>
                              <a href="#">Men's Lookbook</a>
                              <a href="#">Women's Lookbook</a>
                            </div>
                            <div class="column">
                              <h3>YOUR LOOKBOOK</h3>
                              <a href="#">View and Edit</a>
                              <a href="#">Share</a>
                              <a href="#">Delete</a>
                            </div>
                            
                          </div>
                        </div>
                    </div>
                    
                    
                    <div class="dropdown">
                     <li><button class="dropbtn"><a href="{% url 'localStores' %}">LOCAL STORES</a>
                            
                    <i class="fa fa-caret-down"></i>
                  </button></li>
                        <div class="dropdown-content">
                            
                          <div class="row">
                            <div class="column">
                              <h3>OUR LOOKBOOKS</h3>
                              <a href="#">Latest Posts</a>
                              <a href="#">Men's Lookbook</a>
                              <a href="#">Women's Lookbook</a>
                            </div>
                            <div class="column">
                              <h3>YOUR LOOKBOOK</h3>
                              <a href="#">View and Edit</a>
                              <a href="#">Share</a>
                              <a href="#">Delete</a>
                            </div>
                            
                          </div>
                        </div>
                    </div>
                    <div class="dropdown">
                        <li><button class="dropbtn">LOOK BOOK
                            
                          <i class="fa fa-caret-down"></i>
                        </button></li>
                        <div class="dropdown-content">
                            
                          <div class="row">
                            <div class="column">
                              <h3>OUR LOOKBOOKS</h3>
                              <a href="#">Latest Posts</a>
                              <a href="#">Men's Lookbook</a>
                              <a href="#">Women's Lookbook</a>
                            </div>
                            <div class="column">
                              <h3>YOUR LOOKBOOK</h3>
                              <a href="#">View and Edit</a>
                              <a href="#">Share</a>
                              <a href="#">Delete</a>
                            </div>
                            
                          </div>
                        </div>
                    </div>
                    
                    
                </ul> 
                      
                    
                

            </div>
            <div class="right-main-header">
                <span class="search">
                <input class="searchform" type="text" placeholder="Search..">
                <button  class ="searchbutton"type="submit"><i class="fa fa-search"></i></button>
                </span>
            </div>
        </div>

    </div>
`

class Header extends HTMLElement {
    constructor() {
        
        super();
    }

    connectedCallback() {
        const shadowRoot = this.attachShadow({ mode: 'open' });
        shadowRoot.appendChild(headerTemplate.content);
    }
}

customElements.define('header-component', Header);

const footerTemplate = document.createElement('template');
footerTemplate.innerHTML = `
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link href='https://fonts.googleapis.com/css?family=Montserrat' rel='stylesheet'>
<style>
body{
    margin: auto;
}
.footer{
    background-color: f7f7f7;
    height: 550px;
    margin: auto;
    

}
.main-footer{
    display: flex;
    justify-content: space-around;
    padding-left: 50px;
    padding-right: 50px;
    padding-top: 50px;
}
li{
    text-decoration: none;
    padding-top: 10px;
    color: #575153;
    font-family: montserrat;
}
ul{
    list-style-type: none;
    padding: 0;
    
    
}
a{
    text-decoration: none;
    font-family:montserrat; 
    font-size: 13px;

}
h5{
    font-family: montserrat;
    

}
.award{
    background-image:url(./img/award.png) ;
    width: 30%;
    margin-right: 10px;
    display: block;
    text-align: center;
    padding-top: 30px;
    
    color: white;
    
}
.social-icons{
    background-image: url("./img/social-icons.png");
    width: 30%;
    margin-left: 10px;
    text-align: center;
    padding-top: 30px;
    color: white;
    display: flex;
    
}
.right-side-footer{
    width: 20%;
}
.left-side-footer{
    width: 20%;
}
.banner-footer{
    display: flex;
    justify-content: space-between;
    height: 150px;
    margin-top: 20px;
    
}

.fa-facebook {
    
    color: white;
}

.fa-twitter {

color: white;
}

.fa-google {

color: white;
}

.fa-linkedin {

color: white;
}

.fa {
    
    font-size: 30px;
    width: 25%;
    text-align: center;
    text-decoration: none;
    padding-top: 30px;
  }
.copyright-footer{
    display: flex;
    background-color: #333333;
    justify-content: center;
    margin-top: 30px;
}
.copyright{
    align-items: center;
    color: white;
    font-size: 10px;
    width: 50%;
    margin-left: 250px;
}
.design-by{
    align-items: center;
    color: white;
    font-size: 10px;
    width: 50%;
}

@media (max-width:768px) {
    .footer{
      display: block;
    }
    .main-footer{
        display: block;
    }
    .banner-footer{
        display: block;
      }
    .copyright-footer{
        margin-top: 220px;
    }
    .award{
        width: 473px;
        margin-left: 10px;
        height: 140px;
    }
    .social-icons{
        width: 473px;
        height: 140px;
        margin-top: 10px;
        
        
    }
    .fa{
        margin-bottom: 50px;
    }
    
    
  }

</style>

<div class="footer">
        <div class="main-footer">
            <div class="column">
                <h5>INFORMATION</h5>
                <ul class="footer-list">
                    <a href="#"><li>The brand</li></a>
                    <a href="#"><li>Local stores</li></a>
                    <a href="#"><li>Customer service</li></a>
                    <a href="#"><li>Privacy & cookies</li></a>
                    <a href="#"><li>Site map</li></a>
                </ul>
            </div>
            <div class="column">
                <h5>WHY BUY FROM US</h5>
                <ul class="footer-list">
                    <a href="#"><li>Shipping & returns</li></a>
                    <a href="#"><li>Secure shopping</li></a>
                    <a href="#"><li>Testimonials</li></a>
                    <a href="#"><li>Award winning</li></a>
                    <a href="#"><li>Ethical trading</li></a>
                </ul>
            </div>
            <div class="column">
                <h5>YOUR ACCOUNT</h5>
                <ul class="footer-list">
                    <a href="#"><li>Sing in</li></a>
                    <a href="#"><li>Register</li></a>
                    <a href="#"><li>View cart</li></a>
                    <a href="#"><li>View your lookbook</li></a>
                    <a href="#"><li>Track an order</li></a>
                    <a href="#"><li>Update information</li></a>
                </ul>
            </div>
            <div class="column">
                <h5>LOOKBOOK</h5>
                <ul class="footer-list">
                    <a href="#"><li>Latest post</li></a>
                    <a href="#"><li>Men's lookbook</li></a>
                    <a href="#"><li>Women's lookbook</li></a>
                    <a href="#"><li>Lookbooks RSS feed</li></a>
                    <a href="#"><li>View your lookbook</li></a>
                    <a href="#"><li>Delete your lookbook</li></a>
                </ul>
            </div>
            <div class="column">
                <h5>CONTACT DETAILS</h5>
                <ul class="footer-list">
                    <a href="#"><li>HeadOffice:Avenue Fashion</li></a>
                    <a href="#"><li>Telephone:033 123 4567</li></a>
                    <a href="#"><li>Email:example@gmail.com</li></a>
                    
                </ul>
            </div>
        </div>
        <div class="banner-footer">
            <div class="left-side-footer"></div>
            <div class="award">
                <b>AWARD WINNER</b><br><br>
                <p>FASHION AWARDS 2022</p>


            </div>
            <div class="social-icons">
                <a href="#" class="fa fa-facebook"></a>
                <a href="#" class="fa fa-twitter"></a>
                <a href="#" class="fa fa-google"></a>
                <a href="#" class="fa fa-linkedin"></a>

            </div>
            <div class="right-side-footer"></div>
        </div>
        <div class="copyright-footer">
            <p class="copyright">
                &#169;
                Avenue Fashion
    
    
            </p>
            <p class="design-by">
                Design by ITAcademy Begginers :)
            </p>
        </div>
        
            
    </div>
`

class Footer extends HTMLElement {
    constructor() {
        
        super();
    }

    connectedCallback() {
        const shadowRoot = this.attachShadow({ mode: 'open' });
        shadowRoot.appendChild(footerTemplate.content);
    }
}

customElements.define('footer-component', Footer);