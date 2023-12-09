import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SearchComponent } from './search/search.component';
import { ArtObjectListComponent } from './art-object-list/art-object-list.component';
import { ArtObjectDetailComponent } from './art-object-detail/art-object-detail.component';
import { FormsModule } from '@angular/forms';
import { HeaderComponent } from './header/header.component';
import { AboutComponent } from './about/about.component';
import { ReportsComponent } from './reports/reports.component';
import { FooterComponent } from './footer/footer.component';

@NgModule({
  declarations: [
    AppComponent,
    SearchComponent,
    ArtObjectListComponent,
    ArtObjectDetailComponent,
    HeaderComponent,
    AboutComponent,
    ReportsComponent,
    FooterComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }