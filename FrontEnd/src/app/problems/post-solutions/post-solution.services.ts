import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Solution } from './post-solution';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SolutionService {

  private url_: string ='/assets/solutions.json'; // //'https://my-json-server.typicode.com/typicode/demo/comments'

  constructor(private http: HttpClient) {}

  getSolution(): Observable<Solution[]>{
    return this.http.get<Solution[]>(this.url_);
  }
}
