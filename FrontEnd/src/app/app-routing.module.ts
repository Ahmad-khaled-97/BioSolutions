import { NgModule, Component } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { PostProblemComponent } from './problems/post-problem/post-problem.component';
import { PostSolutionComponent } from './problems/post-solutions/post-solution.component';
import { LoginComponent } from './auth/login/login.component';
import { LandingComponent } from './land/land.component';
import { RegisterComponent } from './auth/register/register.component';
import { HubComponent } from './hub/hub.component';
import { HubDownloadComponent } from './hub/hub-download/hub-download.component';
import { HubUploadComponent } from './hub/hub-upload/hub-upload.component';


const routes: Routes = [
  { path: '', component: LandingComponent },
  { path: 'submitproblem', component: PostProblemComponent },
  { path: 'login', component: LoginComponent},
  { path: 'register' , component: RegisterComponent },
  { path: 'problemsolution', component: PostSolutionComponent},
  { path: 'hub' , component: HubComponent },
  { path: 'hubdownload' , component: HubDownloadComponent },
  { path: 'hubupload' , component: HubUploadComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
