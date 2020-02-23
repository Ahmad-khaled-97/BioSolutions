import { Component, OnInit } from '@angular/core';
import { SolutionService } from './post-solution.services';
import { PostProblemComponent } from 'src/app/problems/post-problem/post-problem.component'

@Component({
  selector: 'app-post-solution',
  templateUrl: './post-solution.component.html',
  styleUrls: ['./post-solution.component.css']
})


export class PostSolutionComponent implements OnInit {

constructor(private _solutionservice : SolutionService ) {}

 solutions_arr = [];

ngOnInit() {
  this._solutionservice.getSolution()
      .subscribe(data => this.solutions_arr = data);
}

}
// export class PostSolutionComponent {

// }
