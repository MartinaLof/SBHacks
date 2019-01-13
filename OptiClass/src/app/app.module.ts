import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HomeComponent } from './home/home.component';
import { ResultsComponent } from './results/results.component';

// Angular Material
import {
  MatButtonModule,
  MatCheckboxModule,
  MatSidenavModule,
  MatSliderModule,
  MatCardModule,
  MatDialogModule,
  MatToolbarModule,
  MatInputModule,
  MatFormFieldModule,
  MatIconModule,
  MatGridListModule,
  MatSelectModule,
  MatTableModule,
} from '@angular/material';

import { FilterComponent } from './filter/filter.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ExtracurricularComponent } from './extracurricular/extracurricular.component';
import { ExCurricularComponent } from './extracurricular/ex-curricular/ex-curricular.component';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    HomeComponent,
    ResultsComponent,
    FilterComponent,
    ExtracurricularComponent,
    ExCurricularComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatCheckboxModule,
    MatSidenavModule,
    MatSliderModule,
    MatCardModule,
    FormsModule,
    MatDialogModule,
    MatToolbarModule,
    MatInputModule,
    MatFormFieldModule,
    ReactiveFormsModule,
    MatIconModule,
    MatGridListModule,
    MatSelectModule,
    MatTableModule
  ],
  providers: [],
  bootstrap: [AppComponent],
  entryComponents: [ExtracurricularComponent]
})
export class AppModule { }
