import { Component } from '@angular/core';
import {  HttpClient } from '@angular/common/http';
import { Authservice } from '../auth.service';
import { NgForm } from '@angular/forms';

@Component({
  templateUrl: './register.component.html' ,
  styleUrls: ['./register.component.css']

})
export class RegisterComponent {

  isLoading = false;

  constructor( public authServive: Authservice) {}

  onRegisteration(form:NgForm) {
    if (form.invalid){
      return;
    }

    this.authServive.createUser(form.value.email, form.value.password, form.value.name)
  }




}
