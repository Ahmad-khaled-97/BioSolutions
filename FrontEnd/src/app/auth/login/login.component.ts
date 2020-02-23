import { Component } from '@angular/core';
import { Authservice } from '../auth.service';
import { NgForm } from '@angular/forms';


@Component({
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']

})
export class LoginComponent {
  isLoading = false;

  constructor( public authServive: Authservice) {}

  onLogin(form:NgForm) {
    if (form.invalid){
      return;
    }

    this.authServive.login(form.value.email, form.value.password)
  }

}

// submitUser(usern, passw) {
//   const usr = {
//    emailt : usern,
//    passwordt : passw
//   };

//   console.log(usr);
//   this.http.post(`http://localhost:5000/`, usr).subscribe(res => console.log(res));
// // }
// email = '';
//   password = '';
//   emailt = '';
//   passwordt = '';

//   uri = 'http://localhost:4200/';

//   constructor(private http: HttpClient) { }
