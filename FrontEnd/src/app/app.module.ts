import { BrowserModule } from '@angular/platform-browser';
import { NgModule , Injectable} from '@angular/core';
import { FormsModule } from '@angular/forms';
import {
  MatInputModule,
  MatCardModule,
  MatFormFieldModule,
  MatButtonModule,
  MatToolbarModule,
  MatExpansionModule,
  MatIconModule,
} from '@angular/material';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PostProblemComponent } from './problems/post-problem/post-problem.component';
import { HeaderComponent } from './header/header.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { PostSolutionComponent } from './problems/post-solutions/post-solution.component';
import { LoginComponent } from './auth/login/login.component';
import { RegisterComponent } from './auth/register/register.component';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { LandingComponent } from './land/land.component';
import { HubComponent } from './hub/hub.component';
import { HubDownloadComponent } from './hub/hub-download/hub-download.component';
import { HubUploadComponent } from './hub/hub-upload/hub-upload.component';
import { NgMatSearchBarModule } from 'ng-mat-search-bar';
import { Authservice } from './auth/auth.service';
import { AuthInterceptor } from './auth/auth-interceptor';

@NgModule({
  declarations: [
    AppComponent,
    PostProblemComponent,
    HeaderComponent,
    PostSolutionComponent ,
    LoginComponent,
    RegisterComponent,
    LandingComponent,
    HubComponent,
    HubUploadComponent,
    HubDownloadComponent

  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatInputModule,
    MatCardModule,
    MatFormFieldModule,
    MatButtonModule,
    MatIconModule,
    MatToolbarModule,
    MatExpansionModule,
    HttpClientModule,
    NgMatSearchBarModule,
  ],
  providers: [PostProblemComponent, {provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true}],
  bootstrap: [AppComponent]
})
export class AppModule { }
