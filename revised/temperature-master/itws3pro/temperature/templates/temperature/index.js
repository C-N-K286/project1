(function() {
  var PercentWidget, canvas1, percent,
    bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };

  PercentWidget = (function() {
    var canvas, context, degrees, endAngle, grad, grad1, grad2, percent, radius, startAngle, t, x, y;

    t = canvas = context = grad = radius = null;

    startAngle = endAngle = percent = degrees = null;

    x = y = 0;

    grad1 = {
      0: "#eef3a3",
      1: "#fc6d67"
    };

    grad2 = {
      0: "#77ed7b",
      1: "#00c3b5"
    };

    function PercentWidget(canvas, percent, radius, start) {
      var gradient;
      if (radius == null) {
        radius = 95;
      }
      if (start == null) {
        start = -.25;
      }
      this.update = bind(this.update, this);
      this.canvas = canvas;
      this.context = this.canvas.getContext("2d");
      this.context.font = "20px HelveticaNeue-UltraLight";
      this.context.lineWidth = 2.2;

      /*@context.lineCap = 'round' */
      gradient = grad1;
      if (percent < 50) {
        gradient = grad2;
      }
      this.gradient = gradient;
      this.grad = this.context.createLinearGradient(245, 225, 0, 0);
      this.grad.addColorStop(1, gradient[0]);
      this.grad.addColorStop(0, gradient[1]);
      this.radius = radius;
      this.startAngle = (-.25 * 360) * (Math.PI / 180);
      this.endAngle = 0;
      this.percent = percent;
      this.degrees = (this.percent / 100) * 360;
      this.x = this.canvas.width / 2;
      this.y = this.canvas.height / 2;
    }

    PercentWidget.prototype.reset = function() {
      this.setup(this.canvas, this.percent, this.gradient);
      return this.draw();
    };

    PercentWidget.prototype.draw = function() {
      return this.t = setInterval(this.update, 3);
    };

    PercentWidget.prototype.update = function() {
      var endDegrees, endPercent, radians;
      radians = -(this.degrees * (Math.PI / 180));
      this.endAngle -= 0.01;
      if (this.endAngle < radians) {
        if (this.t != null) {
          return clearTimeout(this.t);
        }
      } else {
        endDegrees = this.endAngle * (180 / Math.PI);
        endPercent = (endDegrees / 360) * 100;
        endPercent = Math.abs(endPercent);
        endPercent = Math.round(endPercent);
        this.context.beginPath();
        this.context.arc(this.x, this.y, this.radius, 0, Math.PI * 2, true);
        this.context.strokeStyle = "#fff";
        this.context.stroke();
        this.context.beginPath();
        this.context.arc(this.x, this.y, this.radius, this.startAngle, this.endAngle + this.startAngle, true);
        this.context.strokeStyle = this.grad;
        this.context.stroke();
        this.context.clearRect(this.x - this.radius + (this.radius / 3), this.y - this.radius + (this.radius / 3), this.radius * 1.4, this.radius);
        return this.context.fillText(endPercent , this.x - (this.radius / 3), this.y);
      }
    };

    return PercentWidget;

  })();

  canvas1 = document.getElementById("canvas1");

  percent = parseInt($('#percent').val());

  new PercentWidget(canvas1, percent).draw();

  $('.js-start').on('click', function() {
    percent = parseInt($('#percent').val());
    return new PercentWidget(canvas1, percent).draw();
  });

}).call(this);
