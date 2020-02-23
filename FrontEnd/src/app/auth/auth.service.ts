import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Authdata } from './auth-data.model';
import { Subject } from 'rxjs';

@Injectable({providedIn: 'root'})

export class Authservice {

  private token: string;
  private authStatusListener = new Subject<boolean>();

  constructor(private http: HttpClient) {}

  getToken(){
    return this.token;
  }

  getAuthStatusListener(){
    return this.authStatusListener.asObservable();
  }

  createUser(email: string, password: string, name: string ){
    const authData: Authdata = {email: email, password:password, name: name}
    this.http.post(`http://localhost:5000/api/users/register`, authData).subscribe(response => {
      console.log(response);
    })
  }

  login(email: string, password: string) {
    // const authData: Authdata = {email: email, password: password}
    // this.http.post<{token: string}>(`http://localhost:5000/api/users/login`, authData).subscribe(response => {
    //   console.log(response);
    //   const token = response.token;
    //   this.token = token;
    //   this.authStatusListener.next(true);

    // })
  }
}
