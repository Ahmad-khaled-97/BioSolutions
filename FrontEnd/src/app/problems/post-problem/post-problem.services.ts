import { Injectable } from '@angular/core';
import { Sol } from 'src/app/problems/post-problem/post-problem';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SolServ {

  constructor() { }

  getStudents(): any {
    const solsObservable = new Observable(observer => {
           setTimeout(() => {
               observer.next(this);
           }, 1000);
    });

    return solsObservable;
}
}



